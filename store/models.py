from django.db import models
from django.contrib.auth.models import User

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
    
