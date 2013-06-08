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

urlpatterns = patterns('blog.views',
    # Blog
    url(r'^$', 'recent', name='blog'),
    # Index
    url(r'^index/$', 'index'),
    # Archives
        # post user
    url(r'^archive/user/(?P<username>\w+)/$', 'archive_user'),
        # post id
    url(r'^archive/id/(?P<post_id>\d+)/$', 'archive_id'),
        # post date
    url(r'^archive/date/(?P<post_year>\d+)/$', 'archive_year'),
    url(r'^archive/date/(?P<post_year>\d+)/(?P<post_month>\d+)/$', 
        'archive_month'),
    url(r'^archive/date/(?P<post_year>\d+)/(?P<post_month>\d+)/(?P<post_day>\d+)/$', 
        'archive_day'),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('blog.views',
    #url(r'^.+$', 'blog'),
#)
