from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = "<h1> This page is forbidden </h1>"
    return HttpResponse(data)