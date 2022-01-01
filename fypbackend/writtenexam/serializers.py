from rest_framework import serializers
from .models import ExamTitle,ExamQuestion


class ExamTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTitle
        fields = ["title"]


class ExamQuestionSerializer(serializers.ModelSerializer):
    exam = ExamTitleSerializer(read_only=True)

    class Meta:
        model = ExamQuestion
        fields = ["exam", "title"]
