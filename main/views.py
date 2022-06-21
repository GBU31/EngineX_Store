from django.shortcuts import render
from .models import *


def home(request):
    items = item.objects.all()
    return render(request, 'home.html', {'items':items})