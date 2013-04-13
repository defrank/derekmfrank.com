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


# Google Webmaster view
def webmaster(request):
  template = 'google0a2e75908547fa0e.html'
  context = {}
  return render_to_response(template, context)


# Home page view
def home(request):
  errors = []
  message = ''
  dt = datetime.datetime.now()
  template = 'home.html'
  context = {
    'errors': errors,
    'message': message,
    'current_datetime': dt
  }
  return response(request, template, context)


# Search page view
def search(request):
  errors = []
  message = ''
  q = None
  if 'q' in request.GET:
    q = request.GET['q']
  if not q:
    errors.append('Specify a search')
  elif len(q) > 200:
    errors.append('Search is too long')
  else:
    message = 'You are searching for "%s"' % request.GET['q']
  template = 'search.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)


# Notifications page view
def notifications(request):
  errors = []
  message = ''
  template = 'notifications.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)


# Friends page view
def friends(request):
  errors = []
  message = ''
  template = 'friends.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)


# Points page view
def points(request):
  errors = []
  message = ''
  template = 'points.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)


# History page view
def history(request):
  errors = []
  message = ''
  template = 'history.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)


# Personal Profile page view
def profile(request):
  errors = []
  message = ''
  template = 'profile.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)
