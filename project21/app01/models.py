from django.db import models

# Create your models here.
class Employee(models.Model):
    idno=models.IntegerField()
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
