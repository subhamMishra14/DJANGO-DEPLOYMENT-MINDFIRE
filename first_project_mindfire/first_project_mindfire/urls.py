"""first_project_mindfire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic_hello_world import views as basic_view
from django.conf.urls import url
from URL_MAPPING_USING_INCLUDE_FUNCTION import views as include_view
from django.conf.urls import include
from TEMPLATES import views as template_view
from STATIC_MEDIA_FILES import views as static_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',basic_view.index,name='index'),
    url(r'^URL_MAPPING_USING_INCLUDE_FUNCTION/',include('URL_MAPPING_USING_INCLUDE_FUNCTION.urls')),
    url(r'^TEMPLATES/',include('TEMPLATES.urls')),
    url(r'^STATIC_MEDIA_FILES/',include('STATIC_MEDIA_FILES.urls'))


]
