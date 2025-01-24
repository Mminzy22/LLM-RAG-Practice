from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserForm
from django.contrib.auth import get_user_model


class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserForm
    success_url = '/accounts/login/'

class LoginView(LoginView):
    template_name = 'accounts/login.html'

class LogoutView(LogoutView):
    pass