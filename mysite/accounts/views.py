# $Id: views.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - accounts
#
# DESCRIPTION
#   Views for accounts (i.e. User Profile).
#

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from utils import response, get_default_user as _user, get_profile_or_user


####
## HELPERS

####
## VIEWS

def user_view(request, template, context):
    """All about views: are about users."""
    if not template:
        template = 'accounts/user.html'
    return response(request, template, context)


def aboutme(request):
    """About homepage: view default user."""
    template = 'accounts/aboutme.html'
    context = {
    }
    return response(request, template, context)


def user(request, username):
    """
    About someone: a specified user.
    
    Takes a username.
    """
    template = 'accounts/user.html'
    context = {
        'myuser': get_profile_or_user(username),
    }
    return response(request, template, context)

