from django.conf.urls import url
from STATIC_MEDIA_FILES import views


urlpatterns=[
            url(r'^$',views.static,name='static')
]
