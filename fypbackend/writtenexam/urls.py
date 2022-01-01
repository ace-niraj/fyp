from django.urls import path
from writtenexam import views

urlpatterns = [
     path("", views.GetExam.as_view()),
     path("q/<str:topic>/", views.ExamQuestions.as_view()),
]
