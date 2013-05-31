# $Id: views.py,v 1.4 2013-05-27 12:40:43-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - aboutme
#
# DESCRIPTION
#   A template views definition for mysite about me.
#

from django.conf import settings
from django.contrib.sites.models import get_current_site

from utils.functions import response
from models import Person, Source, Document


# Helper function to get me
def get_me():
    me = Person.objects.get(id=1)
    return me


# About Me page view
def aboutme(request):
    errors = []
    me = get_me()
    sources = Source.objects.filter(person=me).order_by('priority', 'type')
    documents = Document.objects.filter(person=me).order_by('type', 'title')
    template = 'aboutme.html'
    context = {
        'errors': errors,
        'sources': sources,
        'documents': documents,
    }
    return response(request, template, context)
