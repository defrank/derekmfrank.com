# $Id: views.py,v 1.1 2013-06-11 16:31:46-07 dmf - $
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

from utils import response, get_default_user as _user


####
## HELPERS

def get_profile_or_user(username):
    user = get_object_or_404(User, username__exact=username)
    try:
        profile = user.profile
        return profile
    except Exception:
        return user


####
## VIEWS

def about_view(request, template, context):
    """All about views: are about users."""
    if not template:
        template = 'accounts/about.html'
    return response(request, template, context)


def aboutme(request):
    """About homepage: view default user."""
    u = _user
    try:
        user = u.profile
    except Exception:
        user = u

    template = 'accounts/aboutme.html'
    context = {
        'myuser': user,
    }
    return response(request, template, context)


def aboutmff(request):
    """About MFF"""
    template = 'accounts/aboutmff.html'
    context = {
        'myuser': get_profile_or_user('mff'),
    }
    return response(request, template, context)


def about(request, username):
    """
    About someone: a specified user.
    
    Takes a username.
    """
    #user = get_profile_or_user(username)
    #print user.get_full_name()
    template = 'accounts/about.html'
    context = {
        'myuser': get_profile_or_user(username),
        #'myuser': user,
    }
    return response(request, template, context)

