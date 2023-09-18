from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addGames/<int:pk>/', views.addGames, name='addGames'),
    path('startGame/<int:pk>', views.startGame, name='startGame'),
    path('trackGame/<int:pk>/', views.trackGame, name='trackGame'),
    path('editGame/<int:pk>/', views.editGame, name='editGame'),
    path('gameList/<int:Pk>/', views.gameList, name='gameList'),
]