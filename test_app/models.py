from django.db import models

# Create your models here.
class Student(models.Model):
    hallticket_no=models.TextField(max_length=10,primary_key=True)
    name=models.TextField(max_length=100,default=None)
    year=models.TextField(max_length=100,default=None)
    branch=models.TextField(max_length=100,default=None)