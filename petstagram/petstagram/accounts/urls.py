from django.urls import path, include

from petstagram.accounts.views import register_page, login_page, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('register/', register_page, name='register page'),
    path('login/', login_page, name='login page'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete')
    ]))
]