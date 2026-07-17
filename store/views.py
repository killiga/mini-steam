from django.shortcuts import render
from .models import Game

def games(request):
    games = Game.objects.all()

    return render(request, "games.html", {
    "games": games
})