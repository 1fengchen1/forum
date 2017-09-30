from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","article", "owner", "content", "status", "to_comment", )

admin.site.register(Comment, CommentAdmin)