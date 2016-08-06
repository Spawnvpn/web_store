from django.contrib import admin
from users.models import WebStoreUser


@admin.register(WebStoreUser)
class UserAdmin(admin.ModelAdmin):
    pass