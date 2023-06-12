from django.urls import path

from notes.notes_app.views import home_page, add_note, edit_note, delete_note, details_note, profile_page, \
    delete_profile

urlpatterns = [
    path('', home_page, name='home page'),
    path('add', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile', profile_page, name='profile page'),
    path('profile/delete', delete_profile, name='delete profile')
]