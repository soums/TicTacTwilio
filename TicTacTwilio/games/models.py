from django.db import models

# Create your models here.
class Game(models.Model):
	player_1=models.CharField(max_length=30)
	player_2=models.CharField(max_length=30)

class Move(models.Model):
	game_id=models.ForeignKey(Game)
	location=models.IntegerField(default=0)
	marker=models.CharField(max_length=1)



		
