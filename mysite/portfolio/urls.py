# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - portfolio
#
# DESCRIPTION
#   A url patterns definition for my portfolio.
#

from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    # Portfolio
    url(r'^$', views.portfolio, name='portfolio'),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', views.portfolio),
)
