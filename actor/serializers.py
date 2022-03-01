from rest_framework import  serializers
from .models import  Movie, Actor, Comment
from datetime import date
from rest_framework.exceptions import  ValidationError
from rest_framework.validators import  UniqueForDateValidator

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','year','imdb','genre' ]

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'birthday', 'gender']

    def validate_birthday(self,value):
        if value < date(1950,1,1):
            raise ValidationError(detail='The date must be less than')
        return value

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['movie_id', 'user_id','text', 'created_at']