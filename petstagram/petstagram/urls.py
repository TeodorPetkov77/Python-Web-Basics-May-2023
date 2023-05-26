from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.url')),
    path('accounts/', include('petstagram.accounts.url')),
    path('pets/', include('petstagram.pets.url')),
    path('photos/', include('petstagram.photos.url'))
]
