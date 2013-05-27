# $Id: views.py,v 1.4 2013-05-27 12:40:43-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - mysite
#
# DESCRIPTION
#   A template views definition for mysite derekmfrank.com.
#

from mysite.views.view_functions import response
from django.conf import settings
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
#from django.template.loader import get_template
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.sites.models import get_current_site
import datetime

from mysite.models import Message

# Home page view
def home(request):
  errors = []
  messages = Message.objects.order_by('timestamp').reverse()
  template = 'home.html'
  context = {
    'errors': errors,
    'content_messages': messages,
  }
  return response(request, template, context)


# About Me page view
def aboutme(request):
  errors = []
  dt = datetime.datetime.now()
  template = 'aboutme.html'
  context = {
    'errors': errors,
    'current_datetime': dt
  }
  return response(request, template, context)


# MFF page view
def mff(request):
  errors = []
  dt = datetime.datetime.now()
  template = 'mff.html'
  context = {
    'errors': errors,
    'current_datetime': dt
  }
  return response(request, template, context)
