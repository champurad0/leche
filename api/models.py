from django.db import models
from django.contrib.auth.models import User


class Pump(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time_pumped = models.IntegerField(blank=True, null=True)
    oz_pumped = models.IntegerField(blank=False)
