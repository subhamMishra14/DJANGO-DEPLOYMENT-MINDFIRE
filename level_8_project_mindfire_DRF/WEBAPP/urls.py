from django.urls import path,include
from WEBAPP import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees',views.EmployeeList)

urlpatterns=[
            path('',include(router.urls))
]
