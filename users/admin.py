from django.contrib import admin

# Register your models here.
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, CustomOutstandingTokenAdmin)