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
    url(r'^index/$', 'index', name='index'),
    # Archives
        # entry author
    url(r'^archive/author/$', 'index', name='archive_author'),
    url(r'^archive/author/(?P<username>\w+)/$', 'archive_author'),
        # entry id
    url(r'^archive/id/$', 'index', name='archive_id'),
    url(r'^archive/id/(?P<entry_id>\d+)/$', 'archive_id'),
        # entry date
    url(r'^archive/date/(?P<entry_year>\d+)/$', 'archive_year'),
    url(r'^archive/date/(?P<entry_year>\d+)/(?P<entry_month>\d+)/$', 
        'archive_month'),
    url(r'^archive/date/(?P<entry_year>\d+)/(?P<entry_month>\d+)/(?P<entry_day>\d+)/$', 
        'archive_day'),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('blog.views',
    #url(r'^.+$', 'blog'),
#)
