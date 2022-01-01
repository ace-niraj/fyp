from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class StudentType(models.Model):
    studenttype = models.CharField(max_length=255)

    def __str__(self):
        return self.studenttype


class UserManager(BaseUserManager):
    def create_user(self, username, email, studenttype, password=None):
        if username is None:
            raise TypeError("Username is required")
        if email is None:
            raise TypeError("Email is required")
        user = self.model(
            username=username,
            studenttype=studenttype,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, username="Niraj"):
        if password is None:
            raise TypeError("Password is required")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    studenttype = models.ForeignKey(
        StudentType, blank=True, null=True, on_delete=models.DO_NOTHING
    )
    admin = "admin"
    teacher = "teacher"
    student = "student"

    type = [(admin, "admin"), (teacher, "teacher"), (student, "student")]
    usertype = models.CharField(choices=type, default=student, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email
