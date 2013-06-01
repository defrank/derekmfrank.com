# $Id: urls.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - mff
#
# DESCRIPTION
#   A url patterns definition for MFF pages.
#

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    # MFF
    url(r'^$', views.mff, name='mff'),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', views.mff),
)
