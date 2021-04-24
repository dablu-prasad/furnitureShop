from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    desc=models.TextField()

class CardDetail(models.Model):
    cardnumber=models.CharField(max_length=16,blank=True, null=True)
    cardholdername = models.TextField(max_length=50,blank=True, null=True)
    cvvnumber=models.CharField(max_length=3,blank=True, null=True)
    expmonth=models.CharField(max_length=2,blank=True, null=True)
    expyear=models.CharField(max_length=2,blank=True, null=True)

