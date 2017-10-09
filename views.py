from django.shortcuts import render
from blocks.models import Block
from instationmsg.models import Message

def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    owner = request.user
    msg_cnt = len(Message.objects.filter(owner=owner, status=-1))
    return render(request, 'index.html', {"blocks": block_infos, "msg_cnt":msg_cnt})
