from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam_06_2023.fruit_app.urls')),
    path('', include('exam_06_2023.common_app.urls')),
    path('profile/', include('exam_06_2023.profile_app.urls')),
]
