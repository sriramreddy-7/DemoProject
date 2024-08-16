from django.db import models

# Create your models here.
class Student(models.Model):
    hallticket_no=models.TextField(max_length=10,primary_key=True)
    name=models.TextField(max_length=100,default=None)
    year=models.TextField(max_length=100,default=None)
    branch=models.TextField(max_length=100,default=None)
    
    
class Jobs(models.Model):
    job_title=models.TextField(max_length=100)
    job_description=models.TextField(max_length=1000)
    job_location=models.TextField(max_length=100)
    job_salary=models.TextField(max_length=100)
    job_type=models.TextField(max_length=100)
    link=models.URLField(max_length=1000,default=None)

    def __str__(self):
        return self.job_title
