from django.contrib.auth import get_user_model
from django.db import  models
from .movie import Movie
from datetime import date
from django.utils.timezone import now
User = get_user_model()

class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='movie')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    text =models.TextField()
    created_at = models.DateField(default=now)

