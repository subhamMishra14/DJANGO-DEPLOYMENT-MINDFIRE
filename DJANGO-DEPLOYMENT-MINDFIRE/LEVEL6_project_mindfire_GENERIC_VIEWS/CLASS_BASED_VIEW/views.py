<<<<<<< HEAD
from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.

class Template_View(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["inject_here"]='BASIC_INJECTION'
        return context
=======
from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.

class Template_View(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["inject_here"]='BASIC_INJECTION'
        return context
>>>>>>> e130dfaa52201b6bb61049d31118551875f3a902
