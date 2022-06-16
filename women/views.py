from django.shortcuts import render
from django.http import HttpResponse


def pageNotFound(request, exception):
    return HttpResponse('<h1>Sorry, but something went wrong, see you later!</h1>')


def index(request):
    return HttpResponse('<h1>This is the home page, welcome!</h1>')