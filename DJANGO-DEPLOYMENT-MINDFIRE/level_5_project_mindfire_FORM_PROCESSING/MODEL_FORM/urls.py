from django.conf.urls import url
from MODEL_FORM import views

urlpatterns=[
            url(r'^$',views.ModelForm,name='ModelForm')
]
