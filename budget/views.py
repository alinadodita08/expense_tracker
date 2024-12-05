from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .helpers import password_num, password_special_char
# PEP8 - Python Enhancement Proposal 8 style guide

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# GET, POST
def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        password_repeat = request.POST['password-repeat']
        if password != password_repeat:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        if len(password) < 8:
            return render(request, 'register.html', {'error': 'Password should be at least 8 characters.'})
        if password_num(password) < 3:
            return render(request, 'register.html', {'error': 'Password should have at least 3 numbers.'})
        if password_special_char(password) < 1:
            return render(request, 'register.html', {'error': 'Password should have at least 1 special character.'})
        email = request.POST['email']
        username = request.POST['login']
        if User.objects.filter(username=username).exists():
            return render(request,'register.html', {'error': "Username already exists, please log in"})
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect("login")
    return render(request, 'register.html')


@login_required
def home(request):
    return render(request, 'home.html')