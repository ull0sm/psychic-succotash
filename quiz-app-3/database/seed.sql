-- Insert Users (Students and Teachers)
INSERT INTO users (name, email, password, role, subject) VALUES
('Alice', 'alice@student.com', 'password123', 'student', NULL),
('Bob', 'bob@student.com', 'password123', 'student', NULL),
('Charlie', 'charlie@teacher.com', 'password123', 'teacher', 'DBMS'),
('Diana', 'diana@teacher.com', 'password123', 'teacher', 'Java');

-- Insert Questions for DBMS
INSERT INTO questions (subject, question_text, option1, option2, option3, option4, correct_option) VALUES
('DBMS', 'What does DBMS stand for?', 'Database Management System', 'Data Backup and Management System', 'Data Bank Management Software', 'None of the above', 'Database Management System'),
('DBMS', 'Which of the following is a primary key?', 'Unique Identifier', 'Foreign Key', 'Index Key', 'All of the above', 'Unique Identifier'),
('DBMS', 'What is a foreign key?', 'A unique key in the table', 'A key that references another table', 'A key used for encryption', 'None of the above', 'A key that references another table');

-- Insert Questions for Java
INSERT INTO questions (subject, question_text, option1, option2, option3, option4, correct_option) VALUES
('Java', 'Which company developed Java?', 'Microsoft', 'Sun Microsystems', 'Oracle', 'IBM', 'Sun Microsystems'),
('Java', 'Which keyword is used to create an object in Java?', 'new', 'class', 'object', 'create', 'new'),
('Java', 'Which of these is a valid Java datatype?', 'int', 'Integer', 'float', 'All of the above', 'All of the above');

-- Insert Scores
INSERT INTO scores (user_id, subject, score) VALUES
(1, 'DBMS', 8), -- Alice
(2, 'Java', 7); -- Bob