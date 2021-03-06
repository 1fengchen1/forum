from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "sex", 'birthday', 'avatar')

admin.site.register(UserProfile, UserProfileAdmin)