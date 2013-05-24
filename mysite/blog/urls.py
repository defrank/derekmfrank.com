# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - blog
#
# DESCRIPTION
#   A url patterns definition for my blog.
#

from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    # Blog
    url(r'^$', views.blog, name='blog'),
)
