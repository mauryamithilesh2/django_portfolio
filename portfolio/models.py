from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    contact = models.CharField(max_length=15, default="0000000000")

    def __str__(self):
        return self.name 