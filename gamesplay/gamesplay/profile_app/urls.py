from django.urls import path

from gamesplay.profile_app.views import details_profile, edit_profile, delete_profile, create_profile

urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]