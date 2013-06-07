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
    url(r'^archive/user/(?<username>\w+)/$', 'archive_user'),
        # post id
    url(r'^archive/id/(?<post_id>\d+)/$', 'archive_id'),
        # post date
    url(r'^archive/date/(?<post_year>\d+)/$', 'archive_year'),
    url(r'^archive/date/(?<post_year>\d+)/(?<post_month>\d+)/$', 
        'archive_month'),
    url(r'^archive/date/(?<post_year>\d+)/(?<post_month>\d+)/(?<post_day>\d+)$', 
        'archive_day'),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('blog.views',
    #url(r'^.+$', 'blog'),
#)
