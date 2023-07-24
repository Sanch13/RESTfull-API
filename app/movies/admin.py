from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser, Movie


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title", "genre", "year", "created_date", "update_date",
    )
    list_display = (
        "title", "genre", "year", "created_date", "update_date",
    )
    readonly_fields = (
        "created_date", "update_date",
    )