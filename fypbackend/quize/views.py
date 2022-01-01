from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView


class GetQuiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):
    def get(self, request, form=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[
            :1
        ]
        serializer_class = RandomQuestionSerializer(question, many=True)
        return Response(serializer_class.data)


class QuizQuestion(APIView):
    def get(self, request, form=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs["topic"])
        serializer_class = QuestionSerializer(question, many=True)
        return Response(serializer_class.data)
