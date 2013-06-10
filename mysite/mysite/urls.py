# $Id: urls.py,v 1.6 2013-05-28 22:00:02-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - mysite
#
# DESCRIPTION
#   A url patterns definition for mysite derekmfrank.com.
#

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('mysite.views',
    url(r'^$', 'home', name='home'),
    url(r'^about/$', 'aboutme', name='about'),
    url(r'^about/dmf/$', 'aboutme', name='aboutme'),
    url(r'^about/mff/$', 'aboutmff', name='aboutmff'),
    url(r'^about/(?P<username>\w+)/$', 'about'),
)

urlpatterns += patterns('',
    # Homepage, News Feed
    url(r'^', include('feed.urls')),
    url(r'^feed/', include('feed.urls')),
    # Accounts
    url(r'^accounts/', include('accounts.urls')),
    # Portfolio
    url(r'^portfolio/', include('portfolio.urls')),
    # Blog
    url(r'^blog/', include('blog.urls')),

    # Enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static files
urlpatterns += patterns('django.views.static',
    # Media
    url(r'^static/(?P<path>.*)$', 'serve', { 'document_root': settings.STATIC_ROOT, }),
)

# Media files serve only with DEBUG mode set
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PHP MySQL Database
urlpatterns += patterns('utils',
    url(r'^dh_phpmyadmin.*$', 'redirect_to_mysql', name='mysql'),
    url(r'^mysql.*$', 'redirect_to_mysql'),
)

# Webmasters and other 3rd party apps
urlpatterns += patterns('',
    url(r'^', include('webmaster.urls')),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('',
    #url(r'^.+$', redirect_to_home, name='redirect'),
#)
