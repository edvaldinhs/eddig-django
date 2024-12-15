from django.db import models
from django.contrib import auth

class Player(models.Model):
    name=models.CharField(max_length=100)
    flips=models.IntegerField()
    time=models.IntegerField()
    user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
