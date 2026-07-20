from django.contrib import admin
from django.urls import path
from store import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("games/", views.games, name="games"),
    path("games/<int:id>/", views.game_detail, name="game_detail"),
    path("games/<int:id>/buy/", views.buy_game, name="buy_game"),
    path("library/", views.library, name="library"),
]