from django.shortcuts import render
from form_processing import forms


# Create your views here.

def home(request):
    return render(request,'index.html',context=None)

def form_page(request):
    form=forms.FormName()
    #--------to check data in console------------#
    #----comment it out if not necessary
    '''
    if request.method=="POST":
        form=forms.FormName(request.POST)
    if form.is_valid():
        print("name : "+form.cleaned_data['name'])
    '''
    return render(request,'form_page.html',{'form':form})
