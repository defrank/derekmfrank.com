# $Id: $
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
