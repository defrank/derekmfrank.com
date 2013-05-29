# $Id: view_functions.py,v 1.2 2013-05-17 17:33:56-07 dmfrank - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   functions.py - mysite
#
# DESCRIPTION
#   Functions.
#

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext

# Currently not used, but may be useful
#from django.conf import settings
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import Template, Context
#from django.views.decorators.csrf import csrf_protect
#from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.contrib.sites.models import get_current_site


# Simplified render_to_response() with populated context.
def response(request, template, context):
  """Simplify render_to_response() with context_instance population."""
  return render_to_response(template, context_instance=RequestContext(request, context))
 
# A redirect to home view
def redirect_to_home(request):
  return redirect('/')

# A redirect to php mysql page
def redirect_to_mysql(request):
  return redirect('http://mysql.derekmfrank.com/dh_phpmyadmin/mysqldb.derekmfrank.com/')

# A function to require the user be authenticated/logged in
def require_login(request):
  if not request.user.is_authenticated():
    #return HttpResponseRedirect('/login/?next=%s&username=%s' % (request.path, username))
    return redirect('/accounts/login/?next=%s' % request.path)
  return None
