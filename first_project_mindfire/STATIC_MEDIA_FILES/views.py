from django.shortcuts import render
from STATIC_MEDIA_FILES.media_files import *
from django.http import HttpResponse

# Create your views here.

def static(request):
    return render(request,'index1.html')
