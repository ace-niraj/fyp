from rest_framework import serializers
from .models import StudentScore,ExamUnchecked,ExamChecked


class scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentScore
        fields = ["user", "score", "exam_type"]

class uncheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamUnchecked
        fields = ["user", "question_answer","exam_type"]

class checkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamChecked
        fields = ["user", "question_answer_marks","exam_type"]