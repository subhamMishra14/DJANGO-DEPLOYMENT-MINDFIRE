from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def redirect(request):
    return render(request,'redirect.html')

def other(request):
    return render(request,'other.html')
