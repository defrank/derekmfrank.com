# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - limn
#
# DESCRIPTION
#   Views for User Profile.
#

from django.conf import settings
from django.contrib.sites.models import get_current_site

from django.contrib.auth.models import User

from utils.functions import response, get_default_user
from models import UserProfile


####
## VIEWS

def about_view(request, template, context):
    """All about views: are about users."""
    if not template:
        template = 'about/about.html'
    return response(request, template, context)


def me(request):
    """About homepage: view default user."""
    #user = get_default_user
    template = 'limn/aboutme.html'
    context = {
        #'user': user,
    }
    return response(request, template, context)


def mff(request):
    """About MFF"""
    user = User.objects.get(username='mff')
    template = 'limn/mff.html'
    context = {
        'user': user,
    }
    return response(request, template, context)


def someone(request, username):
    """
    About someone: a specified user.
    
    Takes a username.
    """
    user = User.objects.get(username=username)
    template = 'limn/about.html'
    context = {
        'user': user,
    }
    return response(request, template, context)

