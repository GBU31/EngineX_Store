from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout


def home(request):
    items = item.objects.all()
    return render(request, 'home.html', {'items':items})


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg':'your username or password is incorrect'})

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('home')    