# $Id: urls.py,v 1.1 2013-06-11 16:31:46-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - accounts
#
# DESCRIPTION
#   A url patterns definition for user profiles.
#

from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    # About me
    url(r'^$', 'aboutme'),
    # About a user
    url(r'^(?P<username>\w+)/$', 'user'),
)
