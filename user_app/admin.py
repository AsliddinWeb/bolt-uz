from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'name', 'password', 'is_active')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ['username', 'name', 'id', 'is_staff']
    filter_vertical = ('groups', 'user_permissions',)

admin.site.register(CustomUser, CustomUserAdmin)

# admin.site.register(CustomUser, CustomUserAdmin)
