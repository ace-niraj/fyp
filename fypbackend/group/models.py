from django.db import models


class StudentScore(models.Model):
    user = models.CharField(max_length=50)
    exam_type = models.CharField(max_length=50, default="None")
    score = models.IntegerField()

    def __str__(self):
        return self.user

class ExamUnchecked(models.Model):
    user = models.CharField(max_length=50)
    exam_type = models.CharField(max_length=50, default="None")
    question_answer = models.JSONField({})

    def __str__(self):
        return self.user

class ExamChecked(models.Model):
    user = models.CharField(max_length=50)
    exam_type = models.CharField(max_length=50, default="None")
    question_answer_marks = models.JSONField({})

    def __str__(self):
        return self.user