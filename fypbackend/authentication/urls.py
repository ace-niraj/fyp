from django.urls import path
from .views import RegisterView, VerifyEmail,GetUserView,GetUserTypeView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("getuser/", GetUserView.as_view(), name="getuser"),
    path("getusertype/", GetUserTypeView.as_view(), name="getusertype"),
    path("email_verify/", VerifyEmail.as_view(), name="verify_email"),
]
