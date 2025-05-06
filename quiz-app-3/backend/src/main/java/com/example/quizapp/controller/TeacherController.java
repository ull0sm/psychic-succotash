package com.example.quizapp.controller;

import com.example.quizapp.model.Score;
import com.example.quizapp.service.TeacherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/teacher")
public class TeacherController {

    @Autowired
    private TeacherService teacherService;

    @GetMapping("/students")
    public ResponseEntity<List<StudentScore>> getStudentScores() {
        List<StudentScore> studentScores = teacherService.getAllStudentScores();
        return ResponseEntity.ok(studentScores);
    }
}

// Helper class for student scores
class StudentScore {
    private String name;
    private String subject;
    private int score;

    // Getters and setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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