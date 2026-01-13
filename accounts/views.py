from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']

        if password==confirm:
            try:
                User.objects.create_user(username=email, email=email, password=password)
                messages.success(request, "Account created successfully! Please login.")
                return redirect('login')
            except IntegrityError:
                messages.error(request, "An account with this email already exists.")
        else:
            messages.error(request, "Passwords do not match.")
            
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")
            
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

