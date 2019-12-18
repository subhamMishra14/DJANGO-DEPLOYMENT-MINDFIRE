from rest_framework import serializers
from WEBAPP.models import EmployeeDetails

class EmployeeDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDetails
        fields='__all__'
