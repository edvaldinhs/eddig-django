from django.db import models

class Player(models.Model):
    name=models.CharField(max_length=100)
    flips=models.IntegerField()
    time=models.IntegerField()
