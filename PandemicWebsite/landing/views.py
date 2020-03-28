from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """
    Returns HTTP Response for the home/landing page.
    """
    return HttpResponse('<h1> You are at Landing</h1>')
