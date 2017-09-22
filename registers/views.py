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
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password != repassword:                              #密码不一致的响应提示
            return  render(request, "register.html", {'form':form, "error":"两次密码不一致，请重新输入。"})
        else:
            if form.is_valid():                                 #输入字段符合数据库定义要求的响应
               registerdo = form.save(commit=False)
               registerdo.is_active = False
               registerdo.save()
               return render(request, "register_sucess.html")
            else:                                                #输入字段不符合数据库的要求
                return render(request, "register.html", {"form":form})

