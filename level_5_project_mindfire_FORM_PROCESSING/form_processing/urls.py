from django.conf.urls import url
from form_processing import views

urlpatterns=[
            url(r'^home/$',views.home,name='home'),
            url(r'^form_page/$',views.form_page,name='form_page')
]
