from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os

@login_required
def upload_avatar(request):
    if request.method == "GET":
        return render(request, "upload_avatar.html")
    else:
        user = str(request.user)
        profile = request.user.userprofile                  #OneToOneField的语法糖，可以通过u.userprofile直接访问UserProfile数据表数据
        avatar_file = request.FILES.get("avatar", None)     #获取form表单里的key="avatar‘的上传文件，没有文件就为空；avatar_file是django定义的：文件的对象
        ############文件不能大于2M############
        if avatar_file.size > 2*1024*1024:
            return  render(request, "upload_avatar.html", {'error':'图片大小要小于2M'})
        else:
        ############文件不能大于2M############
            father_path = os.getcwd()     #当前文件的目录
            avatar_path = father_path + "\\userres\\avatar\\"                                    #图片统一存放路径
            name = avatar_file.name.split('.')[1]
            file_name = user + '.' + name                           #修改文件的名字为user.格式
            file_path = os.path.join(avatar_path, file_name)                             #文件存入完整地址
            #print(file_path)

            with open(file_path, 'wb+') as destination:         #以二进制写入的形式('wb+')打开文件
                for chunk in avatar_file.chunks():              #把文件切块，逐块返回，每块(默认64一块)赋值给chunk
                    destination.write(chunk)                    #把每一块写进文件中，写完后with会自动把文件关闭，文件已经写入磁盘中想要的位置了
            url = "http://localhost/userres/avatar/%s" % file_name   #头像的路径
            profile.avatar = url  #avatar,拼写错误
            profile.save()
            return redirect("/")
