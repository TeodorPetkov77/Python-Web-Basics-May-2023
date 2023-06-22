from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gamesplay.common_app.urls')),
    path('game/', include('gamesplay.game_app.urls')),
    path('profile/', include('gamesplay.profile_app.urls')),
]
