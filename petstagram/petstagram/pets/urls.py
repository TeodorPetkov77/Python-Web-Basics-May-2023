from django.urls import path, include

from petstagram.pets.views import pet_add, pet_edit, pet_delete, pet_details

urlpatterns = [
    path('add/', pet_add, name='pet add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', pet_details, name='pet details'),
        path('edit/', pet_edit, name='pet edit'),
        path('delete/', pet_delete, name='pet delete'),
    ]))
]