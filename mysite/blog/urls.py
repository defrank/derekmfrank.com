# $Id: urls.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
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
    url(r'^(\d)/$', views.blogsingle),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', views.blog),
)
