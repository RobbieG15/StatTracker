from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teamManage, name='teamManage'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('orgProfile/<int:pk>/', views.orgProfile, name='orgProfile'),
    path('teamList/<int:pk>/', views.teamList, name='teamList'),
    path('editTeam/<int:pk>/<str:team_name>/', views.editTeam, name='editTeam'),
    path('addTeam/<int:pk>/', views.addTeam, name='addTeam'),
    path('createOrg/', views.createOrg, name='createOrg'),
]