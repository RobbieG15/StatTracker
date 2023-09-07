from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('orgProfile/', views.orgProfile, name='orgProfile'),
    path('teamList/', views.teamList, name='teamList'),
    path('editTeam/', views.editTeam, name='editTeam'),
]