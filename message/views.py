from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Message
from hosting.models import Room


# Create your views here.
def mbox(request,sender):
    messages=Message.objects.all()
    text={}

    for message in messages:
        if message.sender==sender:
            text[message.receiver]=["에게 보낸 쪽지", message.body]
        elif message.receiver==sender:
            text[message.sender]=["에게 받은 쪽지", message.body]

    return render(request, 'mbox.html', {'message':text.items()})


def mdetail(request, sender, receiver):
    messages=Message.objects.all()
    text=[]

    for message in messages:
        if message.sender==sender:
            if message.receiver==receiver:
                text.append(["보낸 쪽지", message.body])
        elif message.receiver==sender:
            if message.sender==receiver:
                text.append(["받은 쪽지", message.body])
    
    text.reverse()

    return render(request,'mdetail.html', {'message':text, 'sender':sender, 'other':receiver})

def new(request, receiver):
    return render(request,'new.html',{'receiver':receiver})

def sendMessage(request):
    message=Message()
    message.sender=request.POST['sender']
    message.receiver=request.POST['receiver']
    message.body=request.POST['body']
    message.time=timezone.datetime.now()
    message.save()
    return redirect('/')