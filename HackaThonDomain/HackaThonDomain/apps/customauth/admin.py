from django.contrib import admin

from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('id','email','date_joined', 'last_login', 'is_admin')
    search_fields = ('email',)
    ordering = ('id','email',)
    readonly_fields = ('date_joined','last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
