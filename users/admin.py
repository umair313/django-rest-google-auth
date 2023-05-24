from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from users.models import User
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
        'password',
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    ordering = ('email',)
    fieldsets = (
        (_('Personal Info'), {
            'fields': (
                'email', 'first_name', 'last_name',
            )
        }),

        (_('Permissions Info'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # (_('Important dates'), {'fields': ('last_login', 'delete_at',)}),
        ('Password Info', {'fields': ('password',)}),
    )
    add_fieldsets = (
        (_('Personal Info'), {
            'fields': (
                'email', 'first_name', 'last_name',
            )
        }),
        (_('Permissions Info'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        ('Password Info', {'fields': ('password1', 'password2')}),
    )
