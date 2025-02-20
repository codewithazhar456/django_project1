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


class author(models.Model):
    author_name=models.CharField(max_length=140)

class book(models.Model):
    author=models.OneToOneField(author,on_delete=models.CASCADE)
    book=models.CharField(max_length=140)



class Brand(models.Model):
    brand=models.CharField(max_length=123)

class products(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.RESTRICT)
    products=models.CharField(123)

