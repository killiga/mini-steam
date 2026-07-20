from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Purchase
from django.contrib.auth.decorators import login_required

def games(request):

    search = request.GET.get("search")

    if search:
        games = Game.objects.filter(
            name__icontains=search
        )
    else:
        games = Game.objects.all()

    return render(request, "store/games.html", {
        "games": games,
        "search": search
    })



def game_detail(request, id):

    game = get_object_or_404(Game, id=id)

    owned = Purchase.objects.filter(
    user=request.user,
    game=game
    ).exists()

    return render(request, "store/game_detail.html", {
    "game": game,
    "owned": owned
    })


@login_required
def buy_game(request, id):

    game = get_object_or_404(Game, id=id)

    if not Purchase.objects.filter(user=request.user, game=game).exists():

        Purchase.objects.create(
            user=request.user,
            game=game
        )


    return redirect("games")


@login_required
def library(request):

    purchases = Purchase.objects.filter(
        user=request.user
    )

    return render(request, "store/library.html", {
        "purchases": purchases
    })