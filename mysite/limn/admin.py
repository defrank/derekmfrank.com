# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - limn
#
# DESCRIPTION
#   Models definition for User Profile.
#

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from limn.models import UserProfile, UserImageInline, UserDocumentInline, UserRepositoryInline, UserProfileInline, UserSourceInline


####
## ADMIN

## User Profile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = u'profile'

class UserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
        UserImageInline, 
        UserDocumentInline, 
        UserRepositorySourceInline, 
        UserProfileSourceInline, 
        UserSourceInline
    ]


####
## REGISTER
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
