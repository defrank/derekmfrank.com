# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
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
## VIEWS

def about_view(request, template, context):
    """All about views: are about users."""
    if not template:
        template = 'accounts/about.html'
    return response(request, template, context)


def aboutme(request):
    """About homepage: view default user."""
    user = _user
    template = 'accounts/aboutme.html'
    context = {
        'user': user,
    }
    return response(request, template, context)


def aboutmff(request):
    """About MFF"""
    user = get_object_or_404(User, username='mff')
    template = 'accounts/aboutmff.html'
    context = {
        'user': user,
    }
    return response(request, template, context)


def about(request, username):
    """
    About someone: a specified user.
    
    Takes a username.
    """
    person = get_object_or_404(User, username='jd')
    template = 'accounts/about.html'
    context = {
        'person': person,
    }
    return response(request, template, context)

