# $Id: views.py,v 1.4 2013-05-27 12:40:43-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - feed
#
# DESCRIPTION
#   A template views definition for mysite derekmfrank.com.
#

from django.conf import settings

from utils.functions import response
from models import Message


# Home page view
def feed(request):
    messages = Message.objects.order_by('timestamp').reverse()
    template = 'home.html'
    context = {
        'content_messages': messages,
    }
    return response(request, template, context)
