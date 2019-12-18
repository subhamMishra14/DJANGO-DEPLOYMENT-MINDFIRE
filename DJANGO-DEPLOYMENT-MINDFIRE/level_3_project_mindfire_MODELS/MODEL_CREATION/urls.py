from django.conf.urls import url
from MODEL_CREATION import views

#app_name=

urlpatterns=[
            url(r'mtv_view/',views.index,name='index')
]
