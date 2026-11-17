from django.db import models

# Create your models here.

class Player(models.Model):
    name=models.CharField(max_length=100)
    photo=models.URLField()
    player_id=models.IntegerField()
    nationality=models.CharField()


class Team(models.Model):
    name=models.CharField(max_length=100)
    crest=models.URLField()