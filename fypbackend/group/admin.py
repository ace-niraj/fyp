from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.StudentScore)
class StudentScore(admin.ModelAdmin):
    list_display = ["user", "score", "exam_type"]

@admin.register(models.ExamUnchecked)
class UncheckedExam(admin.ModelAdmin):
    list_display = ["user","exam_type", "question_answer"]

@admin.register(models.ExamChecked)
class CheckedExam(admin.ModelAdmin):
    list_display = ["user","exam_type", "question_answer_marks"]