from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def myassets(request):
    form = Create()

    if request.method == 'POST':
        form = Create(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.user = request.user
            form2.save()


    items = item.objects.all()
    return render(request, 'myassets.html', {'items':items, 'form':form})