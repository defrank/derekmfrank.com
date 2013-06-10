# $Id: functions.py,v 1.1 2013-05-28 22:00:02-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   __init__.py - mysite
#
# DESCRIPTION
#   Utility functions.
#

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext

from django.contrib.auth.models import User

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


####
## VIEWS

def response(request, template, context):
    """Simplify render_to_response() with context_instance population."""
    return render_to_response(template, context_instance=RequestContext(request, context))

 
def redirect_to_home(request):
    return redirect('/')


def redirect_to_mysql(request):
    return redirect('http://mysql.derekmfrank.com/dh_phpmyadmin/mysqldb.derekmfrank.com/')


def require_login(request):
    if not request.user.is_authenticated():
        #return HttpResponseRedirect('/login/?next=%s&username=%s' % (request.path, username))
        return redirect('/accounts/login/?next=%s' % request.path)
    return None


####
## MODELS

def get_default_user():
    return User.objects.get(pk=1)
