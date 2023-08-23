from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active']
    list_display_links = ['email']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['-date_joined']
    filter_horizontal = []
    last_filter = []
    fieldsets = []