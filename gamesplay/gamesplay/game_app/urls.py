from django.urls import path

from gamesplay.game_app.views import create_game, details_game, edit_game, delete_game

urlpatterns = [
    path('create/', create_game, name='create game'),
    path('details/<int:pk>/', details_game, name='details game'),
    path('edit/<int:pk>/', edit_game, name='edit game'),
    path('delete/<int:pk>/', delete_game, name='delete game'),

]