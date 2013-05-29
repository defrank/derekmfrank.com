# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - aboutme
#
# DESCRIPTION
#   A url patterns definition for my about me.
#

from django.conf.urls import patterns, url
from aboutme import views

urlpatterns = patterns('',
    # About me
    url(r'^$', views.aboutme, name='aboutme'),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', views.aboutme),
)
