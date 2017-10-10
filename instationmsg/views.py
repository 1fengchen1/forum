from .models import Message
from comments.jsonresponse import json_response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#信息列表页面数据展示
@login_required
def unreadmsg(request):
    owner = request.user
    unmsgs = Message.objects.filter(owner=owner, status=-1)
    return render(request, 'message_list.html', {'unmsgs':unmsgs})

#jQuery处理已查看的信息
@login_required
def readmsg(request):
    id = request.POST["id"]
    Message.objects.filter(id=id).update(status=1)
    sucess = {"status": "ok"}
    return json_response(sucess)