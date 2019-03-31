from django.shortcuts import render
from django.http import HttpResponse

def results(request):
    return HttpResponse("hello")
