from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name
    

class Purchase(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.game}"
    

class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    game = models.ForeignKey(
    Game,
    on_delete=models.CASCADE,
    related_name="reviews"
    )
    rating = models.IntegerField(
    validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user} - {self.game}"