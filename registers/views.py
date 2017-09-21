from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .froms import RegisterForm

def register(request):
    parameter = {"username":User.username, "password":User.password,
                 "email":User.email}
    if request.method == "GET":
        return render(request, "register.html")
    else:
        form = RegisterForm(request.POST)
        if form.is_valid() and password == repassword:
           registerdo = form.save(commit=False)
           registerdo.password =
           registerdo.save()
           return redirect("/")
        else:
            return render(request, "register.html", parameter)

