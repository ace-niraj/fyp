from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.ExamCategory)
class CatExamAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.ExamTitle)
class ExamTitleAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(models.ExamQuestion)
class ExamQuestionAdmin(admin.ModelAdmin):
    fields = ["title", "exam"]
    list_display = ["title", "exam", "date_updated"]
    


