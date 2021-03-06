'''
This file handles all logic related to authentication and signing up
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import BusinessForm
from django.contrib import messages
def registerUser(request):
    '''
    registerUser goes hand-in-hand with signup. registerUser captures info from signup and adds the user to the database,
    then logs them in.
    '''
    username = request.POST['username']
    password = request.POST['password']

    verify = authenticate(username=username,password=password)
    if verify is not None:
        #The user is in the database, log them in
        print("asd")
    else:
        #The user is not in the database. Register them by creating a new user and adding to the database
        user = User.objects.create_user(username=username,password=password)


    return redirect('changed:index')
def auth(request):
    #authenticates and logs in the user
    username = request.POST['username']
    password = request.POST['password']

    if len(username)==0 or len(password)==0 :
        messages.error(request,'Please enter a non-blank username or password')
        return redirect('changed:index')
    verify = authenticate(username=username,password=password)
    if verify is not None:
        #The user is in the database, log them in
        login(request,verify)
        form = BusinessForm()
        context={
            'user':verify,
            'form':form,
        }
        return render(request,'changed/home.html',context)
    else:
        #The user is not in the database. Register them by creating a new user and adding to the database
        #user = User.objects.create_user(username=username,password=password)
        messages.error(request,'Invalid username or password')
        return redirect('changed:index')

def logout(request):
    auth_logout(request)
    return redirect('changed:index')