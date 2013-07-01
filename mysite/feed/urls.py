# $Id: urls.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - feed
#
# DESCRIPTION
#   A url patterns definition for mysite news feed.
#

from django.conf.urls import patterns, url


urlpatterns = patterns('feed.views',
    # Homepage News Feed
    url(r'^$', 'feed', name='feed'),
)
