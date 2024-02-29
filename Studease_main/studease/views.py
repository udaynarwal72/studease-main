from django.shortcuts import render,HttpResponse,redirect
#added manually
from datetime import datetime
from studease.models import contact
#added manually to display allert messages..
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
def index(request):
    #variable can be sent through this method..
    #context is a dictonary of variables
    context={
            "variable":"this is sent"
    }
    #this is used to flash message on the web page
    # if request.method =="POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     Contact = contact(email = email,name = name,date = datetime.today())
    #     Contact.save()
    #     messages.success(request, "this is a text message")
    print(request.user)
    if request.user.is_anonymous:
        return HttpResponse("Hello")
    return render(request,'index.html',context)
# Create your views here.
#we use HttpResponse to render string directly..
def loginUser(request):
    if request.method =="POST":
        username =request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    # A backend authenticated the credentials
        else:
            return render(request,'login.html')
    # No backend authenticated the credentials
        
    print(request.user)

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")