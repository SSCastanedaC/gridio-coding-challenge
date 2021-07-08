from django.db import models

# Create your models here.

class FinlandMarketPrice(models.Model):
    date = models.DateField()
    time = models.IntegerField()
    price = models.FloatField()

class EstoniaMarketPrice(models.Model):
    date = models.DateField()
    time = models.IntegerField()
    price = models.FloatField()