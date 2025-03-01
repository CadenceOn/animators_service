from django.contrib import admin
from .models import User, Request

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'date_joined')
    list_filter = ('role',)
    search_fields = ('username', 'email')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'status', 'parent', 'animator')
    list_filter = ('status', 'date')
    search_fields = ('description',)