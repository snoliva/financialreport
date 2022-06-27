from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    #class Meta:
    #    verbose_name = _("")
    #    verbose_name_plural = _("s")

    def __str__(self):
        return self.name

class Revenues(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Spends(models.Model):
    
    TYPES_CATEGORY = [
        ("H", 'House'),
        ("S", 'Supermarket'),
        ("I", "Investment"),
        ("R", "Rent"),
        ("M", "Mortage"),
        ("T", "Travel"),
        ("C", "Card"),
        ("L", "Light"),
        ("W", "Water"),
        ("CE", "Celphone"),
        ("IN", "Internet"),
        ("ST", "Streaming"),
        ("M", "Medical"),
        ("P", "Party")
    ]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=TYPES_CATEGORY, blank=True, null=True)
    cost = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Savings(models.Model):

    TYPES_CATEGORY = [
        ("F", 'Funds'),
        ("C","Crypto"),
    ]

    ENTERPRISES = [
        ("R", "Racional"),
        ("D", "DVA"),
        ("F", "Fintual"),
        ("S", "Soy Focus"),
        ("B", "Binance")
    ]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=TYPES_CATEGORY, blank=True, null=True)
    real_price = models.FloatField()
    enterprise = models.CharField(max_length=100, blank=True, choices=ENTERPRISES, null=True)
    quantity = models.FloatField()
    total_investment = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self):
        self.total_investment = self.quantity * self.real_price
        super(Savings, self).save()