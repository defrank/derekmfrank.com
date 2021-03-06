# $Id: urls.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank
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
    # Archives
    url(r'^archive/all/$', 'blog', name='blog_all'),
        # entry author
    url(r'^archive/author/(?P<username>\w+)/$', 'archive_author'),
        # entry id
    url(r'^archive/id/(?P<id>\d+)/$', 'archive_id'),
        # entry date
    url(r'^archive/date/(?P<year>\d+)/$', 'archive_year'),
    url(r'^archive/date/(?P<year>\d+)/(?P<month>\d+)/$', 
        'archive_month'),
    url(r'^archive/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 
        'archive_day'),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('blog.views',
    #url(r'^.+$', 'blog'),
#)
