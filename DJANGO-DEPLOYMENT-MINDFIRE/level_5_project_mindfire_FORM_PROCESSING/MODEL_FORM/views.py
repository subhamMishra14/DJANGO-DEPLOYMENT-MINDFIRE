from django.shortcuts import render
from MODEL_FORM import forms
from form_processing import views

# Create your views here.

def ModelForm(request):
    form = forms.UserForm()

    if request.method=="POST":
        print("HI")
        form=forms.UserForm(request.POST)

        if form.is_valid():
            print("Hello")
            form.save()

            return views.home(request)
    '''

    '''
    return render(request,'model_form_page.html',{'form':form})
