from django.urls import path
from . import views
from .spoftify import *

urlpatterns = [
    path('', views.home),
    path('cawilo', views.home,name='cawilo'),
     path('room', views.RoomView.as_view()),
    path('check',IsAuthenticated,name='check'),
    path('ali', views.RoomView.as_view()),
    path('join', views.joinRoom,name='joinRoom'),
    path('create', views.createRoom,name='createRoom'),
    path('create-room', views.CreateRoomView.as_view(),name='createR'),
    path('get-room', views.GetRoom.as_view()),
    path('join-room', views.JoinRoom.as_view(),name = 'join-room'),
    path('user-in-room', views.UserInRoom.as_view()),
    path('leave-room', views.LeaveRoom.as_view()),
    path('update-room', views.UpdateRoom.as_view()),
    path('get-auth-url', AuthURL, name='get-auth-url'),
    path('redirect', spotify_callback, name='redirect'),
    path('current-song', CurrentSong, name='current-song'),
]