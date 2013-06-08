# $Id: urls.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - portfolio
#
# DESCRIPTION
#   A url patterns definition for my portfolio.
#

from django.conf.urls import patterns, url

urlpatterns = patterns('porject.views',
    # Portfolio
    url(r'^$', 'portfolio', name='portfolio'),
    url(r'^(?P<username>\w+)/$', 'someone'),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('',
    #url(r'^.+$', views.portfolio),
#)
