from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('howToList/', views.howToList, name='howToList'),
    path('FAQ/', views.howToList, name='FAQ'),
    path('help/', views.howToList, name='help'),
    path('about/', views.howToList, name='about'),
]