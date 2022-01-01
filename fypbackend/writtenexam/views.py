from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import ExamQuestion, ExamTitle
from .serializers import ExamTitleSerializer,ExamQuestionSerializer

class GetExam(generics.ListAPIView):
    serializer_class = ExamTitleSerializer
    queryset = ExamTitle.objects.all()

class ExamQuestions(APIView):
    def get(self, request, format=None, **kwargs):
        exam = ExamQuestion.objects.filter(exam__title=kwargs["topic"])
        serializer_class = ExamQuestionSerializer(exam, many=True)
        return Response(serializer_class.data)
