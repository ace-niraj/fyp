from django.urls import path
from group import views

urlpatterns = [
    path("get_group/", views.GetGroup.as_view()),
    path("score/", views.ScoreView.as_view()),
    path("uncheckedscore/", views.ExamUncheckedView.as_view()),
    path("checkedscore/", views.ExamCheckedView.as_view()),
]
