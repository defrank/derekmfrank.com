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


# About Me page view
def aboutme(request):
  errors = []
  me = Person.objects.get(id=1)
  template = 'aboutme.html'
  context = {
    'errors': errors,
    'me': me,
  }
  return response(request, template, context)
