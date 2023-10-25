from django.db import models

class GameState(models.Model):
    next_player = models.IntegerField(default=1)
    winner = models.IntegerField(default=None, null=True)
    board = models.JSONField(max_length=200)

    def to_json(self):
        return {
            "id": self.id,
            "next_player": self.next_player,
            "winner": self.winner,
            "board": self.board,
        }
