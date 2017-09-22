from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .froms import RegisterForm

def sucess(request):
    return HttpResponse("Success")

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
           registerdo = form.save(commit=False)
           registerdo.is_active = False
           registerdo.save()
           return render(request, "register_sucess.html")
        else:
            return render(request, "register.html", {"form":form})

