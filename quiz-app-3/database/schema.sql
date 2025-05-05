-- Users Table
CREATE TABLE users (
    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL, -- Ensure passwords are hashed
    role ENUM('student', 'teacher') NOT NULL,
    subject VARCHAR(50) -- Only for teachers
);

-- Questions Table
CREATE TABLE questions (
    question_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(50) NOT NULL,
    question_text TEXT NOT NULL,
    option1 VARCHAR(100) NOT NULL,
    option2 VARCHAR(100) NOT NULL,
    option3 VARCHAR(100) NOT NULL,
    option4 VARCHAR(100) NOT NULL,
    correct_option VARCHAR(100) NOT NULL
);

-- Scores Table
CREATE TABLE scores (
    score_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    subject VARCHAR(50) NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);