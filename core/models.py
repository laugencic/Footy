
from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=100)
    crest=models.URLField() 
    team_id=models.CharField(max_length=20,unique=True)
    # trophies=models.ManyToManyField(blank=True,null=True,related_name='team_trophies')

    def __str__(self):
        return f"{self.name} details"
    
class Player(models.Model):
    name=models.CharField(max_length=100)
    photo=models.URLField(blank=True,null=True)
    player_id=models.CharField(max_length=20,unique=True)
    nationality=models.CharField(max_length=20)
    # teams_played=models.ManyToManyField(Team,related_name='former_teams')
    # milestones=models.ManyToManyField(blank=True,null=True,related_name='player_milestones')

    def __str__(self):
        return f"{self.name} details"

