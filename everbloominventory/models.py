from django.db import models

class Inventory(models.Model):
    product = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    card = models.CharField(max_length=100)