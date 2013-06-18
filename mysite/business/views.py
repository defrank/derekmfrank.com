# $Id: views.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - business
#
# DESCRIPTION
#   A template views definition for user business pages.
#

from django.conf import settings
from django.contrib.sites.models import get_current_site

from utils import response, get_profile_or_user


####
## VIEWS

def user(request, username):
    """
    Business view for a user.

    Takes a username.
    """
    template = 'business/business.html'
    context = {
        'myuser': get_profile_or_user(username),
    }
    return response(request, template, context)
