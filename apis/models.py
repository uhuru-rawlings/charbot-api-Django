from django.db import models

# Create your models here.
class Regisreation(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=13)
    userimage = models.ImageField(upload_to = 'images/')
    password = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_loggedin = models.BooleanField(default=True)

    class Meta:
        db_table = 'Regisreation'

    def __str__(self):
        return self.username

class Contacts(models.Model):
    user = models.ForeignKey(to, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=13)

    class Meta:
        db_table = 'Contacts'