from django.urls import path
from user.views import Registration, login, logout
from django.shortcuts import redirect

urlpatterns = [
    path("signin/", Registration.as_view(), name="signin_page"),
    path("login/", login, name="login_page"),
    path("logout/", logout, name="logout_page"),
    path("", lambda request: redirect("/user/login/")),
]
