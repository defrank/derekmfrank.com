# $Id: urls.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - limn
#
# DESCRIPTION
#   A url patterns definition for user profiles.
#

from django.conf.urls import patterns, url

urlpatterns = patterns('limn.views',
    # About me
    url(r'^$', 'me', name='about'),
    # About mff
    url(r'^mff/$', 'mff', name='mff'),
    # About someone
    url(r'^(?P<username>\w+)/$', 'someone'),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('limn.views',
    #url(r'^.+$', 'about'),
#)
