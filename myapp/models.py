from django.db import models

# Create your models here.
class mymessage(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    title= models.TextField(max_length=200)
    message= models.TimeField(max_length=200)
