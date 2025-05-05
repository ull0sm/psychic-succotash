document.addEventListener('DOMContentLoaded', () => {
    const subject = sessionStorage.getItem('selectedQuiz');
    document.getElementById('subject').textContent = subject;

    // Fetch questions for the selected quiz
    fetch(`/quiz/${subject}`)
        .then(response => response.json())
        .then(questions => startQuiz(questions))
        .catch(error => console.error('Error fetching quiz questions:', error));
});

function startQuiz(questions) {
    let currentQuestionIndex = 0;
    let score = 0;
    let timer;

    const questionContainer = document.getElementById('question-container');
    const timerElement = document.getElementById('time-left');

    // Display the first question
    displayQuestion(questions[currentQuestionIndex]);

    // Timer logic
    function startTimer() {
        let timeLeft = 10; // 10 seconds
        timer = setInterval(() => {
            timerElement.textContent = timeLeft;
            if (timeLeft === 0) {
                clearInterval(timer);
                nextQuestion();
            }
            timeLeft--;
        }, 1000);
    }

    function displayQuestion(question) {
        questionContainer.innerHTML = `
            <h2>${question.questionText}</h2>
            <div>
                <button onclick="selectAnswer('${question.option1}', '${question.correctOption}')">${question.option1}</button>
                <button onclick="selectAnswer('${question.option2}', '${question.correctOption}')">${question.option2}</button>
                <button onclick="selectAnswer('${question.option3}', '${question.correctOption}')">${question.option3}</button>
                <button onclick="selectAnswer('${question.option4}', '${question.correctOption}')">${question.option4}</button>
            </div>
        `;
        startTimer();
    }

    function selectAnswer(selectedOption, correctOption) {
        clearInterval(timer);
        if (selectedOption === correctOption) {
            score++;
        }
        nextQuestion();
    }

    function nextQuestion() {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            displayQuestion(questions[currentQuestionIndex]);
        } else {
            endQuiz();
        }
    }

    function endQuiz() {
        questionContainer.innerHTML = `
            <h2>Quiz Completed!</h2>
            <p>Your score: ${score}/${questions.length}</p>
            <button onclick="submitScore(${score}, '${subject}')">Submit Score</button>
        `;
    }
}

function submitScore(score, subject) {
    const userId = sessionStorage.getItem('userId'); // Assuming user ID is stored in sessionStorage
    fetch('/quiz/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userId, score, subject }),
    })
        .then(response => response.json())
        .then(data => {
            alert('Score submitted successfully!');
            window.location.href = 'leaderboard.html';
        })
        .catch(error => console.error('Error submitting score:', error));
}