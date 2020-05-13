from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(required):
    return HttpResponse("CONTACTS")


def about(required):
    return HttpResponse("ABOUT")
