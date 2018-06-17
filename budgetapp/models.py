from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    addr = models.CharField(max_length=100)

class Expenses(models.Model):
    income = models.PositiveIntegerField(null=True)
    house = models.PositiveIntegerField(null=True)
    utility = models.PositiveIntegerField(null=True)
    grocery = models.PositiveIntegerField(null=True)
    transport = models.PositiveIntegerField(null=True)
    health = models.PositiveIntegerField(null=True)
    entertainment = models.PositiveIntegerField(null=True)
    debt = models.PositiveIntegerField(null=True)
    others = models.PositiveIntegerField(null=True)

class SplitBill(models.Model):
    fname=models.CharField(max_length=50)
    pnum=models.PositiveIntegerField()
    addrs=models.CharField(max_length=100)
    amt=models.PositiveIntegerField()

