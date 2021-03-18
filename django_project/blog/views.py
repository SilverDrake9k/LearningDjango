from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#handle from home page of blog
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

#handles the about page
def about(request):
    return HttpResponse('<h1>Blog About</h1>')