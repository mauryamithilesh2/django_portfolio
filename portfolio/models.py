from django.db import models

# Create your models here.
class Clients(models.Model):
    name=models.CharField(max_length=60,null=False,blank=False)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=15, blank=True, null=True)
