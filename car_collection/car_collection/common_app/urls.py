from django.urls import path

from car_collection.common_app.views import index_page, catalogue

urlpatterns = [
    path('', index_page, name="index page"),
    path('catalogue/', catalogue, name="catalogue")
]