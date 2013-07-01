# $Id: urls.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - business
#
# DESCRIPTION
#   A url patterns definition for user business pages.
#

from django.conf.urls import patterns, url

urlpatterns = patterns('business.views',
    # Businesses
    url(r'mff/$', 'mff', name='mff'),
    url(r'(?P<username>\w+)/$', 'user'),
)
