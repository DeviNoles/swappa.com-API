from django.db import models

# Create your models here.
class Phone(models.Model):
    title = models.CharField(max_length=250)
    city = models.CharField(max_length=500)
