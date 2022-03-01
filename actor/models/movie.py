from django.db import models
from .actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    year =  models.DateField()
    imdb = models.CharField(max_length=3)
    genres = [
        ('Advanture', 'Advanture'),
        ('Comedy', 'Comedy'),
        ('Crime','Crime'),
        ('Historical', 'Historical'),
        ('Fantasy', 'Fantasy'),
        ('Horror','Horror' ),
        ('Romance', 'Romance'),
        ('Other', 'Other')
    ]
    genre = models.CharField(max_length=15, choices=genres)
    actors = models.ManyToManyField(Actor, related_name='actors')

    def __str__(self):
        return  self.name