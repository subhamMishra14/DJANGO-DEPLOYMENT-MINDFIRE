from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def include_func(request):
    return HttpResponse("<h1> USING INCLUDE FUNCTION FOR URL MAPPING</h1>")
