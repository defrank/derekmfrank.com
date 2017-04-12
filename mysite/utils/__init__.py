# $Id: __init__.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank
#
# NAME
#   __init__.py - utils
#
# DESCRIPTION
#   Utility functions.
#

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
import markdown

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
## MODEL HELPERS

def get_default_user():
    user = get_object_or_404(User, pk=1)
    try:
        profile = user.profile
        return profile
    except Exception:
        return user


def get_profile_or_user(username):
    user = get_object_or_404(User, username__exact=username)
    try:
        profile = user.profile
        return profile
    except Exception:
        return user


def markdown_to_html(markdownText, images):
    """Function to parse and add image in html format to a blog post"""
    # create instance of Markdown class
    if images:
        md = markdown.Markdown()
        for image in images:
            image_url = image.get_absolute_url()
            # append image reference to Markdown instance
            # md.references[id] = (url, title)
            md.references[image.filename()] = (image_url, '%s' % image.filename())
        # parse source text
        return md.convert(markdownText)
    else:
        return markdownText
