from django.shortcuts import render
from MODEL_CREATION.models import Topic,WebPage,AccessRecord

# Create your views here.

def index(request):
    wepgList=WebPage.objects.all()
    dict_list={'Data_webpage':wepgList}
    return render(request,'MTV/index.html',context=dict_list)
