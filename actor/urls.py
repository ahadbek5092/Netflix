from django.urls import path, include
from .views import ActorViewSet, MovieViewSet,MovieActorAPIView, CommentApiView#,DeleteComment
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actors', ActorViewSet, basename='actors')
# router.register('comments', CommentApiView, basename='comments')
from rest_framework.authtoken import  views
urlpatterns = [
    path('', include(router.urls)),
    path("movies/<int:id>/actors/",MovieActorAPIView.as_view()),
    path('comments/', CommentApiView.as_view()),
    path('auth/', views.obtain_auth_token),
    # path('comments/<int:id>/', DeleteComment.as_view()),

]