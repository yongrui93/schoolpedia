from django.contrib import admin
from sso.models import User
from django.contrib.auth.admin import UserAdmin


class EmailUserAdmin(UserAdmin):
    add_fieldsets = ((None, {'fields': ('username', 'email',
                                        'password1', 'password2'), 'classes': ('wide',)}),)


admin.site.register(User,
                    EmailUserAdmin)
