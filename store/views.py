from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Purchase
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def logout_user(request):

    logout(request)

    return redirect("games")


def login_user(request):

    if request.method == "POST":

        form = AuthenticationForm(
            data=request.POST
        )

        if form.is_valid():

                login(
                    request,
                    form.get_user()
                )

                return redirect("games")
    
    else:

        form = AuthenticationForm()

    return render(
        request,
        "store/login.html",
        {
            "form": form
        }
    )



def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = UserCreationForm()

    return render(request, "store/register.html", {
        "form": form
    })


def games(request):

    search = request.GET.get("search")
    sort = request.GET.get("sort")

    if search:
        games = Game.objects.filter(
            name__icontains=search  
        )
    else:
        games = Game.objects.all()


    if sort == "price_asc":
        games = games.order_by("price")

    elif sort == "price_desc":
        games = games.order_by("-price")

    elif sort == "date":
        games = games.order_by("-release_date")


    return render(request, "store/games.html", {
        "games": games,
        "search": search
    })



def game_detail(request, id):

    game = get_object_or_404(Game, id=id)

    owned = False

    if request.user.is_authenticated:
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