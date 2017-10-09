from .models import Message
from comments.jsonresponse import json_response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def unreadmsg(request):
    owner = request.user
    unmsgs = Message.objects.filter(owner=owner, status=-1)
    return render(request, 'message_list.html', {'unmsgs':unmsgs})

@login_required
def readmsg(request):
    id = request.POST["id"]
    Message.objects.filter(id=id).update(status=1)
    sucess = {"status": "ok"}
    return json_response(sucess)