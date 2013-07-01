# $Id: urls.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - portfolio
#
# DESCRIPTION
#   A url patterns definition for my portfolio.
#

from django.conf.urls import patterns, url

urlpatterns = patterns('portfolio.views',
    # Portfolio
    url(r'^$', 'portfolio', name='portfolio'),
    url(r'^(?P<username>\w+)/$', 'user'),
)
