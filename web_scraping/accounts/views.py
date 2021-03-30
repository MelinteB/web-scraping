from django.shortcuts import render
from django.contrib.auth.views import LoginView

class LoginViewCustom(LoginView):
    template_name = 'accounts/login.html'

