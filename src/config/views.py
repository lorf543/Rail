from django.http import HttpResponse
from django.shortcuts import render

def home_page_vew(request, *args, **kwargs):

    return render (request,'home.html')