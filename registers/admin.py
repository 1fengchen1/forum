from django.contrib import admin
from registers.models import ActivateCode

class CodeKeyAdmin(admin.ModelAdmin):
    list_display = ("username", "activation_code")

admin.site.register(ActivateCode, CodeKeyAdmin)