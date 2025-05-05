package com.example.quizapp.controller;

import com.example.quizapp.model.Question;
import com.example.quizapp.service.QuizService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/quiz")
public class QuizController {

    @Autowired
    private QuizService quizService;

    @GetMapping("/{subject}")
    public ResponseEntity<List<Question>> getQuestionsBySubject(@PathVariable String subject) {
        List<Question> questions = quizService.getQuestionsBySubject(subject);
        return ResponseEntity.ok(questions);
    }

    @PostMapping("/submit")
    public ResponseEntity<String> submitQuiz(@RequestBody QuizSubmission submission) {
        boolean isSubmitted = quizService.submitQuiz(submission);
        if (isSubmitted) {
            return ResponseEntity.ok("Quiz submitted successfully!");
        } else {
            return ResponseEntity.badRequest().body("Failed to submit quiz!");
        }
    }
}

// Helper class for quiz submissions
class QuizSubmission {
    private Long userId;
    private String subject;
    private int score;

    // Getters and setters
    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
}