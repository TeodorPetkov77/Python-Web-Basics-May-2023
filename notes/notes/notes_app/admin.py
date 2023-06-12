from django.contrib import admin

from notes.notes_app.models import Profile, Note

admin.site.register(Profile)
admin.site.register(Note)