from django.conf.urls import url
from TEMPLATES import views

urlpatterns=[
            url(r'^$',views.template_view,name='template_view')
]
