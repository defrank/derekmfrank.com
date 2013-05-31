# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - blog
#
# DESCRIPTION
#   A url patterns definition for my blog.
#

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    # Blog
    url(r'^$', views.blog, name='blog'),
    url(r'^(\d)/$', views.post_detail),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', views.blog),
)
