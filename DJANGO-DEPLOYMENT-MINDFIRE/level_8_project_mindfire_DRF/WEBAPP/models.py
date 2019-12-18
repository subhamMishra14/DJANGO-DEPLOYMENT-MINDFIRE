from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)
    empId=models.IntegerField()

    def __str__(self):
        return self.firstName
        
