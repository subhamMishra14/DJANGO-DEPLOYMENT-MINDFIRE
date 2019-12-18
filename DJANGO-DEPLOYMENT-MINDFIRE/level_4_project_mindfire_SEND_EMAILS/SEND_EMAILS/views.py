from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request,'email/index.html',context=None)

def send_email(request):
    subject='Django mail'
    message='trying to send mail'
    from_email=settings.EMAIL_HOST_USER
    to_list=['subham.mishra14@gmail.com']

    send_mail(subject,message,from_email,to_list,fail_silently=False)

    return render(request,'email/send_email.html',context=None)
