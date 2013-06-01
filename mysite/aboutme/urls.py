# $Id: urls.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - aboutme
#
# DESCRIPTION
#   A url patterns definition for my about me.
#

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    # About me
    url(r'^$', views.aboutme, name='aboutme'),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', views.aboutme),
)
