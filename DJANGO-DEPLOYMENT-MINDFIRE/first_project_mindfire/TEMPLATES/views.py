from django.shortcuts import render
from django.http import HttpResponse
from TEMPLATES.template_static_files import *
# Create your views here.

def template_view(request):
    dict_template={'template_insert_here':"DATA IS COMING FROM VIEWS.PY FILE DYNAMICALLY"}
    return render(request,'index.html',context=dict_template)
