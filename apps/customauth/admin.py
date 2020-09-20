from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import get_user_model

from django_admin_jqueryui_tabs.mixins import ModelAdminTabsMixin

User = get_user_model()


class CustomUserAdmin(ModelAdminTabsMixin, UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined'),
        }),
    )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
