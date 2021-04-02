from django.db import models

# Create your models here.
class Pizza(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField(max_length=500)
    price=models.IntegerField()

class Salad(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField(max_length=500)
    price=models.IntegerField()

class Noodle(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField(max_length=500)
    price=models.IntegerField()