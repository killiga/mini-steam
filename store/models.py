from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name