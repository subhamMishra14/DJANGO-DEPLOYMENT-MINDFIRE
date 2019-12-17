from django.conf.urls import url
from WEBPAGE_REDIRECTING import views

app_name='WEBPAGE_REDIRECTING'

urlpatterns=[
            url(r'^redirect/$',views.redirect,name='redirect'),
            url(r'^other/$',views.other,name='other')
]
