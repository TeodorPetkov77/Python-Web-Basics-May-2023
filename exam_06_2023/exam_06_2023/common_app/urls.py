from django.urls import path

from exam_06_2023.common_app.views import index_page, dashboard

urlpatterns = [
    path('', index_page, name='index page'),
    path('dashboard/', dashboard, name='dashboard')
]