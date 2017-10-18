from django import forms
from django.contrib.auth.models import User
from usercenter.models import UserProfile

'''注册校验'''
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["birthday",]
