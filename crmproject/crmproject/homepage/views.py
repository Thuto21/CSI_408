from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def crm_home(response):
    return render(response, "homepage.html/", {})
