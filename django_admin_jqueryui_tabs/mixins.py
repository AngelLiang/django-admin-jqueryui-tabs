from django.contrib import admin


class ModelAdminTabsMixin(admin.ModelAdmin):
    change_form_template = 'admin/jqueryui_tabs/change_form.html'


class TabularInlineTabsMixin(admin.TabularInline):
    template = 'admin/jqueryui_tabs/edit_inline/tabular.html'


class StackedInlineTabsMixin(admin.StackedInline):
    template = 'admin/jqueryui_tabs/edit_inline/stacked.html'
