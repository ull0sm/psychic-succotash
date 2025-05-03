from flask import Flask, request, jsonify, session, redirect, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from .db.connection import get_db_connection
from datetime import timedelta
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this secret key for production
app.permanent_session_lifetime = timedelta(days=1)

# Enable CORS for frontend localhost
CORS(app, supports_credentials=True)

# Helper function for DB queries
def query_db(query, args=(), one=False, commit=False):
    conn = get_db_connection()
    if conn is None:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    if commit:
        conn.commit()
    if query.lower().startswith('select'):
        rv = cursor.fetchall()
        cursor.close()
        conn.close()
        return (rv[0] if rv else None) if one else rv
    else:
        cursor.close()
        conn.close()
        return None

# Authentication decorator
def login_required(role=None):
    def decorator(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'message': 'Authentication required'}), 401
            if role and session.get('role') != role:
                return jsonify({'message': 'Unauthorized - wrong role'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Registration Route
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')
    password = data.get('password')
    extra_data = data.get('extra_data', {})  # For students/teachers additional info

    if not all([name, email, role, password]) or role not in ['student', 'teacher']:
        return jsonify({'message': 'Missing or invalid fields'}), 400

    # Check if user exists
    existing_user = query_db('SELECT * FROM users WHERE email=%s', (email,), one=True)
    if existing_user:
        return jsonify({'message': 'User with this email already exists'}), 409

    password_hash = generate_password_hash(password)
    insert_user_query = 'INSERT INTO users (name, email, role, password_hash) VALUES (%s, %s, %s, %s)'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_user_query, (name, email, role, password_hash))
    user_id = cursor.lastrowid

    if role == 'student':
        class_name = extra_data.get('class', '')
        subject_assigned = extra_data.get('subject_assigned', '')
        biodata = extra_data.get('biodata', '')
        insert_student_query = 'INSERT INTO students (user_id, class, subject_assigned, biodata) VALUES (%s, %s, %s, %s)'
        cursor.execute(insert_student_query, (user_id, class_name, subject_assigned, biodata))
    elif role == 'teacher':
        subjects_handled = extra_data.get('subjects_handled', '')
        insert_teacher_query = 'INSERT INTO teachers (user_id, subjects_handled) VALUES (%s, %s)'
        cursor.execute(insert_teacher_query, (user_id, subjects_handled))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Registration successful'})

# Login Route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing email or password'}), 400

    user = query_db('SELECT * FROM users WHERE email = %s', (email,), one=True)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'message': 'Invalid email or password'}), 401

    session.permanent = True
    session['user_id'] = user['id']
    session['name'] = user['name']
    session['role'] = user['role']

    # For students, also store student_id
    if user['role'] == 'student':
        student = query_db('SELECT * FROM students WHERE user_id = %s', (user['id'],), one=True)
        if student:
            session['student_id'] = student['student_id']

    return jsonify({'message': 'Login successful', 'role': user['role'], 'name': user['name']})

# Logout Route
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'})

# Get Top Scorers Leaderboard
@app.route('/api/leaderboard', methods=['GET'])
@login_required()
def leaderboard():
    query = """
    SELECT u.name, s.subject, MAX(qs.score) as top_score 
    FROM quiz_scores qs
    JOIN students s ON qs.student_id = s.student_id
    JOIN users u ON s.user_id = u.id
    GROUP BY qs.student_id, qs.subject
    ORDER BY top_score DESC
    LIMIT 10;
    """
    result = query_db(query)
    return jsonify(result or [])

# Get Student List for Teacher with optional subject filter
@app.route('/api/students', methods=['GET'])
@login_required('teacher')
def students_list():
    subject_filter = request.args.get('subject')
    base_query = """
    SELECT st.student_id, u.name, st.class, st.subject_assigned, st.biodata 
    FROM students st 
    JOIN users u ON st.user_id = u.id
    """
    params = ()
    if subject_filter:
        base_query += " WHERE st.subject_assigned = %s"
        params = (subject_filter,)
    students = query_db(base_query, params)
    return jsonify(students or [])

# Get Student's individual scores by teacher request
@app.route('/api/student_scores/<int:student_id>', methods=['GET'])
@login_required('teacher')
def student_scores(student_id):
    query = """
    SELECT subject, score, attempted_on 
    FROM quiz_scores WHERE student_id = %s ORDER BY attempted_on DESC
    """
    scores = query_db(query, (student_id,))
    return jsonify(scores or [])

# Get average scores per subject for analytics - teacher only
@app.route('/api/analytics/average_scores', methods=['GET'])
@login_required('teacher')
def average_scores():
    query = """
    SELECT subject, AVG(score) as average_score FROM quiz_scores GROUP BY subject
    """
    avg_scores = query_db(query)
    return jsonify(avg_scores or [])

# Get quiz questions by subject - student only
@app.route('/api/questions/<subject>', methods=['GET'])
@login_required('student')
def get_questions(subject):
    query = """
    SELECT question_id, question_text, option_a, option_b, option_c, option_d FROM questions WHERE subject = %s ORDER BY RAND() LIMIT 10
    """
    questions = query_db(query, (subject,))
    return jsonify(questions or [])

# Submit quiz score - student only
@app.route('/api/submit_score', methods=['POST'])
@login_required('student')
def submit_score():
    data = request.json
    subject = data.get('subject')
    score = data.get('score')
    student_id = session.get('student_id')

    if not all([subject, isinstance(score, int), student_id]):
        return jsonify({'message': 'Invalid submission'}), 400

    insert_query = """
    INSERT INTO quiz_scores (student_id, subject, score) VALUES (%s, %s, %s)
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_query, (student_id, subject, score))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Score submitted successfully'})

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)