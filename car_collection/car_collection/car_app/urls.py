from django.urls import path, include

from car_collection.car_app.views import car_create, car_details, car_edit, car_delete

urlpatterns = [
    path('create/', car_create, name='car create'),
    path('<int:pk>/', include([
        path('details/', car_details, name='car details'),
        path('edit/', car_edit, name='car edit'),
        path('delete/', car_delete, name='car delete'),
    ]))
]