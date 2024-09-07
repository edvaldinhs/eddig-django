from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('ranking/', views.ranking, name='ranking'),
    path('about/', views.about, name='about'),
    path('basicRank/', views.basicRank, name="basicRank"),
    path('get/', views.get, name="get"),
    path('add/', views.add, name="add"),
    path('delete/<int:id>/', views.delete, name="delete"),
]