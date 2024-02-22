from django.db import models

class Contact2(models.Model):
    name2 = models.CharField(max_length=122)
    email2 = models.CharField(max_length=122)
    phone2 = models.CharField(max_length=12)
class Res(models.Model):
    Restaurant=models.CharField(max_length=122)

# Create your models here.
