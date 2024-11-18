from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField
    age = models.IntegerField

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField
    size = models.DecimalField
    description = models.CharField
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title