from django.db import models

# Create your models here.
class Regisreation(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=13)
    userimage = models.ImageField(upload_to = 'images/')