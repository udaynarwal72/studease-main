from django.shortcuts import render,HttpResponse
#added manually
from datetime import datetime
from studease.models import contact
#added manually to display allert messages..
from django.contrib import messages
# Create your views here.
#we use HttpResponse to render string directly..
def index(request):
    #variable can be sent through this method..
    #context is a dictonary of variables
    context={
            "variable":"this is sent"
    }
    #this is used to flash message on the web page
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact = contact(email = email,name = name,date = datetime.today())
        Contact.save()
        messages.success(request, "this is a text message")
    return render(request,'index.html',context)