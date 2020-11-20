from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:character_id>/player/', views.player, name='player'),
    path('create/', views.create, name='create'),
]