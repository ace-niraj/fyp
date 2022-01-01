from django.contrib import admin
from . import models


@admin.register(models.StudentType)
class StudentType(admin.ModelAdmin):
    list_display = ["studenttype"]


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "usertype",
        "studenttype",
        "is_verified",
        "is_staff",
        "is_active",
        "created_at",
        "updated_at",
    ]
