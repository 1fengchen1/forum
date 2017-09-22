from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block", "title", "content", "owner")

admin.site.register(Article, ArticleAdmin)