# $Id: views.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - webmaster
#
# DESCRIPTION
#   Template views for webmasters.
#

from django.conf import settings
from django.shortcuts import render_to_response


# Google Webmaster view
def google(request):
    template = 'webmaster/google0a2e75908547fa0e.html'
    context = {}
    return render_to_response(template, context)


# Bing Webmaster view
def bing(request):
    template = 'webmaster/BingSiteAuth.xml'
    context = {}
    return render_to_response(template, context)
