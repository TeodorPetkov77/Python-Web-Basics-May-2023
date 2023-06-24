from django.urls import path

from exam_06_2023.profile_app.views import create_profile, details_profile, delete_profile, edit_profile

urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]