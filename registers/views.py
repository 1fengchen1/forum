from django.shortcuts import render
from django.http import HttpResponse
from .froms import RegisterForm
from django.core.mail import send_mail
from .models import ActivateCode
from django.contrib.auth.models import User
import uuid

'''注册'''
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        form = RegisterForm(request.POST)                                                       # 校验器实例化
        ########两次密码不一致########
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password != repassword:                                                              # 密码不一致的响应提示
            return  render(request, "register.html", {'form':form, "error":"两次密码不一致，请重新输入。"})
        ########两次密码不一致########
        else:
            if form.is_valid():                                                                  # 输入字段符合数据库定义要求的响应
                registerdo = form.save(commit=False)
                registerdo.is_active = False
                ########激活码链接发送到邮箱########
                activation_code = str(uuid.uuid4()).replace("-", "")                             # 激活码
                activation_url = "http://%s/approve/%s" % (request.get_host(), activation_code)  # 激活码链接
                activate_email = "点击<a href='%s'>这里</a>激活" % activation_url                 # 邮件信息内容
                username = request.POST["username"]
                email = request.POST["email"]
                code=ActivateCode(username=username, activation_code=activation_code)
                send_mail(subject='[Python技术栈]激活邮件',                                        # 发送邮箱格式
                         message='点击链接激活：%s' % activation_url,                              # 文本内容
                         html_message=activate_email,
                         from_email='758896823@qq.com',
                         recipient_list=[email],                                                  # 用户邮箱列表
                         fail_silently=False)
                ########激活码链接发送到邮箱########
                code.save()                                                                       # 保存到激活码表
                registerdo.save()                                                                 # 保存到用户表
                return render(request, "register_sucess.html")
            else:                                                                                 # 输入字段不符合数据库的要求
                return render(request, "register.html", {"form":form})


'''认证邮箱'''
def approveemil(code):
    db = ActivateCode.objects.all().values('activation_code')                                     # 列表包裹字典类型
    db_code = [key for item in db for key in item.values()]
    if code in db_code:
        username = ActivateCode.objects.get(activation_code=code)                                 # 获得用户名
        User.objects.filter(username=username).update(is_active=True)                             # 激活账户
        return HttpResponse("你的邮箱已认证成功！")
    else:
        return HttpResponse("邮箱认证失败！")