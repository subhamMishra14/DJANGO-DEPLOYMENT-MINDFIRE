#------it is in applications urls.py file
"""
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


from django.conf.urls import include
from django.conf.urls import url
from URL_MAPPING_USING_INCLUDE_FUNCTION import views

urlpatterns=[
        url(r'^$',views.include_func,name='include_func')
]
