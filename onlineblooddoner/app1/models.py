from django.db import models
class Donor(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30)
    age=models.FloatField()
    weigth=models.FloatField()
    blood_group=models.CharField(max_length=20)
    contact=models.IntegerField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
class User(models.Model):
    uname=models.CharField(max_length=30)
    uemail=models.EmailField(primary_key=True)
    password=models.CharField(max_length=20)
class Admin(models.Model):
    uname=models.CharField(max_length=20)
    up=models.CharField(max_length=20,default=False)

