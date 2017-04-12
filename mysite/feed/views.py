# $Id: views.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank
#
# NAME
#   views.py - feed
#
# DESCRIPTION
#   A template views definition for mysite derekmfrank.com.
#

from django.conf import settings

from utils import response
from models import News 


# Home page view
def feed(request):
    feed = News.objects.all()
    template = 'home.html'
    context = {
        'feed': feed,
    }
    return response(request, template, context)
