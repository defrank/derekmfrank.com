# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - accounts 
#
# DESCRIPTION
#   Models definition for User Profile.
#

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from models import UserProfile


####
## ADMIN

## User Profile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0
    can_delete = False
    verbose_name_plural = u'profile'

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Important dates', {
            'fields': ('last_login', 'date_joined',),
            'classes': ('collapse',),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
            'classes': ('collapse',),
        }),
    )
    inlines = (
        UserProfileInline,
    )


####
## REGISTER
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
