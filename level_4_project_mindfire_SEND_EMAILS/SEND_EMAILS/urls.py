from django.conf.urls import url
from SEND_EMAILS import views

app_name='email_app'

urlpatterns=[
            url(r'^home/',views.index,name='index'),
            url(r'^send_email/',views.send_email,name='send_email')
]
