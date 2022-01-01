from django.urls import path
from quize import views

urlpatterns = [
    path("", views.GetQuiz.as_view()),
    path("r/<str:topic>/", views.RandomQuestion.as_view()),
    path("q/<str:topic>/", views.QuizQuestion.as_view()),
]
