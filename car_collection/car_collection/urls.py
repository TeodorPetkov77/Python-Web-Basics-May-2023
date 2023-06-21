from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car_collection.common_app.urls')),
    path('car/', include('car_collection.car_app.urls')),
    path('profile/', include('car_collection.profile_app.urls')),
]
