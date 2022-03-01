from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Actor, Movie, Comment
from .serializers import ActorSerializer, MovieSerializer, CommentSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework import  filters


class CommentApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request,*args, **kwargs):
        comments = Comment.objects.filter(user = self.request.user)
        ser = CommentSerializer(comments, many=True)
        return Response(data=ser.data)

    def post(self, request,*args, **kwargs):
        data = request.data
        newcom = Comment.objects.create(
            movie_id= data['movie_id'],
            user_id= data['user_id'],
            text= data['text'],
            created_at=data['created_at']
        )
        newcom.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request,*args, **kwargs):
        id = request.data['id']
        com = Comment.objects.get(id =id)
        com.delete()
        com.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
# class DeleteComment(APIView):
#     def delete(self, request, *args,**kwargs):
#         id = request.data.get['id']
#         com =Comment.objects.get(id=id)
#         com.delete()
#         com.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'year', 'genre']
    ordering_fields = ['imdb', '-imdb']


    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        # id = request.data.get('id')
        id = request.data['id']
        movie = self.get_object()
        actor = Actor.objects.get(id=id)
        movie.actors.add(actor)
        movie.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    # @action(detail=True, methods=['GET'])
    # def actor_list(self, request, *args, **kwargs):
    #     movie = self.get_object()
    #     actors =movie.actors.all()
    #     ser = ActorSerializer(actors, many=True)
    #     return Response(data=ser.data)

    @action(detail=True, methods=['DELETE'])
    def remove_actor(self, request, *args, **kwargs):
        id = request.data['id']
        movie = self.get_object()
        movie.actors.remove(id)
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieActorAPIView(APIView):

    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        actors =movie.actors.all()

        ser = ActorSerializer(actors, many=True)
        return Response(data=ser.data)

# class ActorApiView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         ser = ActorSerializer(actors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         ser = ActorSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)