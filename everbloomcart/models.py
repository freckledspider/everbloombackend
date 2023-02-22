from django.db import models

class Cart(models.Model):
    product = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    card = models.CharField(max_length=100)