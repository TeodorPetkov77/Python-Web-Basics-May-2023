from django.shortcuts import render
from django.urls import include, path

from exam_06_2023.fruit_app.views import fruit_details, fruit_edit, fruit_delete, create_fruit

urlpatterns = [
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/', include([
        path('details/', fruit_details, name='fruit details'),
        path('edit/', fruit_edit, name='fruit edit'),
        path('delete/', fruit_delete, name='fruit delete'),
    ]))
]
