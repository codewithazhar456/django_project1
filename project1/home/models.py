from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=15)
    age=models.CharField(max_length=3)
    mobile_num=models.CharField(max_length=12)
    gmail=models.models.EmailField( max_length=32)
    date_of_birth=models.models.DateField
    created_at=models.DateTimeField(auto_created=True)
    updated_at=models.DateTimeField(auto_now_add=True)