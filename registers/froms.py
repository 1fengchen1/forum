from django import forms
from django.contrib.auth.models import User

'''注册校验'''
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


