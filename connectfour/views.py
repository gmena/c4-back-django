from django.http import JsonResponse
from .models import GameState

WIN_COUNT = 4
ROW_COUNT = 6
COLUMN_COUNT = 7

def index(request):
    gamestate = GameState(
        next_player=1,
        winner=None,
        board=[[0] * COLUMN_COUNT] * ROW_COUNT,
    )

    gamestate.save()

    return JsonResponse(gamestate.to_json(), safe=False)
