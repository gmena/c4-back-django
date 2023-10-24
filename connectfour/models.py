from django.db import models

class GameState(models.Model):
    next_player = models.IntegerField(default=1)
    winner = models.IntegerField(default=None, null=True)
    board = models.CharField(max_length=200)
