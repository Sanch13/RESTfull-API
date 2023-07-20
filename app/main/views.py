from django.shortcuts import render
from django.contrib.auth.models import AbstractUser


def index(request):
    return render(request, "main/index.html")
