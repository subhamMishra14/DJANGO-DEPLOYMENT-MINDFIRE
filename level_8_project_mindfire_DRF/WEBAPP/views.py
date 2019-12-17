from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from WEBAPP.models import EmployeeDetails
from WEBAPP.searilizer import EmployeeDetailsSerializers
from rest_framework import viewsets

# Create your views here.
'''
class EmployeeList(APIView):
    def get(self,request):
        emp=EmployeeDetails.objects.all()
        changes for routers

        searilizer=EmployeeDetailsSerializers(emp,many=True)
        return Response(searilizer.data)

    def post(self):
        pass

'''

class EmployeeList(viewsets.ModelViewSet):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeDetailsSerializers
