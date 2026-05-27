from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    eaddress = models.CharField(max_length=200)
    