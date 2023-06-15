from django.urls import path

from myplant.myplant_app.views import home_page, show_catalogue, create_plant, details_plant, edit_plant, delete_plant, \
    create_profile, details_profile, edit_profile, delete_profile

urlpatterns = [
    path('', home_page, name='home page'),
    path('catalogue/', show_catalogue, name='show catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', details_plant, name='details plant'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    ]
