from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """Домашняя страница"""
    return render(request, 'lists/home.html')
