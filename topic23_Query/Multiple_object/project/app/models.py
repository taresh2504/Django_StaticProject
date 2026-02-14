from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Age=models.IntegerField()
    City=models.CharField(max_length=20)