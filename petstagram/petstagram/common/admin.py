from django.contrib import admin

from petstagram.common.models import Like, Comment

admin.site.register(Comment)
admin.site.register(Like)
