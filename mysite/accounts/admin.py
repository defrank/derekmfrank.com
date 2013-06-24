# $Id: admin.py,v 1.1 2013-06-11 16:31:46-07 dmf - $
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

from models import UserProfile, Image


####
## INLINE

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1
    can_delete = False
    verbose_name_plural = u'profile'

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


####
## ADMIN

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
        ImageInline,
    )


####
## REGISTER
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
