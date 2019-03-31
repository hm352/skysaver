from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View

class form(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("this is a form page")
    
    def post(self, request, *args, **kwargs):
        return redirect("/results")
        

def results(request):
    return HttpResponse("hello")
