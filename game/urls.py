from django.urls import path
from . import views

urlpatterns = [
    path('', views.guessing_game, name='guessing_game'),
]
