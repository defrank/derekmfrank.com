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

from django.contrib.admin import User

from utils.functions import response
from models import UserProfile


####
## HELPERS

def get_default_user():
    return User.objects.get(id=1)


####
## VIEWS

def about_view(request, template, context):
    """All about views: are about users."""
    if not template:
        template = 'about/about.html'
    return response(request, template, context)


def me(request):
    """About homepage: view default user."""
    profile = get_default_user()
    template = 'limn/about.html'
    context = {
        'profile': profile,
    }
    return response(request, template, context)


def someone(request, username):
    """
    About someone: a specified user.
    
    Takes a username.
    """
    profile = User.objects.get(username=username)
    template = 'limn/mff.html'
    context = {
        'profile': profile,
    }
    return response(request, template, context)

