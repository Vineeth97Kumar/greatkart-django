from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()

admin.site.register(Account,AccountAdmin)


