# $Id: views.py,v 1.4 2013-05-27 12:40:43-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - mysite
#
# DESCRIPTION
#   A template views definition for mysite derekmfrank.com.
#

from django.conf import settings
"""
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.sites.models import get_current_site
"""

from utils.functions import response, get_default_user
from feed.views import feed


####
## VIEWS

def home(request):
    return feed(request)
    """
    me = get_default_user
    template = 'home.html'
    context = {
        'me': me,
    }
    return response(request, template, context)
    """
