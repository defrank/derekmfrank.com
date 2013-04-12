from view_functions import response, require_login
from django.conf import settings
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
#from django.template.loader import get_template
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login as user_login, logout as user_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import get_current_site
import datetime


# Account page view
def account(request):
  errors = []
  message = ''
  template = 'accounts/account.html'
  context = {
    'errors': errors,
    'message': message,
  }
  return response(request, template, context)


# Login page view
def login(request, redirect_field_name=REDIRECT_FIELD_NAME, 
               authentication_form=AuthenticationForm):
  """Displays the login form ahd handles the login action."""
  errors = []
  message = ''
  next = request.GET.get('next', '/home/')
  #if 'next' in request.GET:
    #next = request.GET['next']
  redirect_to = redirect_field_name
  if request.method == "POST":
    message = "entered post"
    form = authentication_form(data=request.POST)
    if form.is_valid():
      # Ensure the user-originating redirection url is safe.
      #if not is_safe_url(url=redirect_to, host=request.get_host()):
        #redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
      # Okay, security check complete. Log the user in.
      user_login(request, form.get_user())
      if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
      # Success, so redirect to previous page
      return HttpResponseRedirect(next)
    else:
      errors.append('Invalid authentication')
  else:
    form = authentication_form(request)
  request.session.set_test_cookie()
  current_site = get_current_site(request)
  template = 'accounts/login.html'
  context = {
    'errors': errors,
    'message': message,
    'form': form,
    redirect_field_name: redirect_to,
    'site': current_site,
    'site_name': current_site.name,
    'next': next,
  }
  return response(request, template, context)


# Logout view
def logout(request):
  user_logout(request)
  template = '/accounts/logged_out/'
  # Redirect to a success page
  return redirect(template)


# Logged out page view
def logged_out(request):
  errors = []
  template = 'accounts/logged_out.html'
  context = {
    'errors': errors,
  }
  return response(request, template, context)


# Settings page view
def settings(request):
  auth_test = require_login(request)
  if auth_test:
    return auth_test
  errors = []
  message = ''
  template = 'accounts/settings.html'
  context = {
    'errors': errors,
    'message': message
  }
  return response(request, template, context)
