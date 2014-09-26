from django.contrib import admin

from orchestra.admin import SelectPluginAdminMixin
from orchestra.apps.accounts.admin import AccountAdminMixin

from .models import SaaS
from .services import SoftwareService


class SaaSAdmin(SelectPluginAdminMixin, AccountAdminMixin, admin.ModelAdmin):
    list_display = ('description', 'service', 'account_link')
    list_filter = ('service',)
    plugin = SoftwareService
    plugin_field = 'service'


admin.site.register(SaaS, SaaSAdmin)
