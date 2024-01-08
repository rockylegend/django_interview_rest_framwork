from django.db import models

# Create your models here.

class UserInformationModal(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    fullName=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=300,blank=True, null=True)
    city=models.CharField(max_length=120,blank=True, null=True)
    state=models.CharField(max_length=100,blank=True, null=True)
    country=models.CharField(max_length=100, blank=True,null=True)
    pincode=models.CharField(max_length=6, blank=True,null=True)
    
    
    
    
    
class ContentModal(models.Model):
    title=models.CharField(max_length=30)
    body=models.TextField()
    summary=models.TextField()
    category=models.CharField(max_length=120)
    primaryKey=models.CharField(max_length=120)
    
    
class UserLogin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.email + self.password