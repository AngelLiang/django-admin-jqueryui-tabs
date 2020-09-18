from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from django_admin_jqueryui_tabs.mixins import ModelAdminTabsMixin

User = get_user_model()


class CustomUserAdmin(ModelAdminTabsMixin, UserAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
