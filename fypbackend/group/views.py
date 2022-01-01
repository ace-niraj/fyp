from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from django.core import serializers
import json
from rest_framework import status
from .serializers import scoreSerializer,uncheckedSerializer,checkedSerializer
from .models import StudentScore, ExamUnchecked,ExamChecked


class GetGroup(APIView):
    def get(self, request, format=None):
        try:
            data = serializers.serialize("json", request.user.groups.all())
            val = json.loads(data)
            return Response(
                {"message": "success", "user": val[0].get("fields").get("name")},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"message": "Server Error"}, status=status.HTTP_400_BAD_REQUEST
            )


class ScoreView(APIView):
    def get(self, request, format=None):
        data = serializers.serialize("json", StudentScore.objects.all())
        val = json.loads(data)
        return Response(val)

    def post(self, request, format=None):
        user = str(request.user)
        save_data = {
            "user": user,
            "score": request.data.get("score"),
            "exam_type": request.data.get("exam_type"),
        }
        serializer = scoreSerializer(data=save_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"})

class ExamUncheckedView(APIView):
    def get(self, request, format=None):
        data = serializers.serialize("json", ExamUnchecked.objects.all())
        val = json.loads(data)
        return Response(val)

    def post(self, request, format=None):
        user = str(request.user)
        save_data = {
            "user": user,
            "question_answer": request.data.get("question_answer"),
            "exam_type": request.data.get("exam_type"),
        }
        
        serializer = uncheckedSerializer(data=save_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"})


class ExamCheckedView(APIView):
    def get(self, request, format=None):
        data = serializers.serialize("json", ExamChecked.objects.all())
        val = json.loads(data)
        return Response(val)

    def post(self, request, format=None):
        
        ExamUnchecked.objects.get(user = str(request.user),exam_type = request.data.get("exam_type")).delete()
        # delUser = ExamUnchecked.objects.filter(val[0].get('fields').get('user') == str(request.user))
        # print(delUser)

        user = str(request.user)
        save_data = {
            "user": user,
            "question_answer_marks": request.data.get("question_answer_marks"),
            "exam_type": request.data.get("exam_type"),
        }
        
        serializer = checkedSerializer(data=save_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success"})