# $Id: urls.py,v 1.10 2013-06-17 17:48:24-07 dmf - $
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


urlpatterns = patterns('',
    # Homepage, News Feed
    url(r'^$', 'feed.views.feed', name='home'),
    url(r'^feed/', include('feed.urls')),
    # Accounts, About
    url(r'^about/$', 'accounts.views.aboutme', name='aboutme'),
    url(r'^user/', include('accounts.urls')),
    # Portfolio
    url(r'^portfolio/', include('portfolio.urls')),
    # Blog
    url(r'^blog/', include('blog.urls')),
    # Business
    url(r'^business/', include('business.urls')),

    # Enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static files
#urlpatterns += patterns('django.views.static',
    # Media
    #url(r'^static/(?P<path>.*)$', 'serve', { 'document_root': settings.STATIC_ROOT, }),
    #url(r'^media/(?P<path>.*)$', 'serve', { 'document_root': settings.MEDIA_ROOT, }),
#)

# Media files serve only with DEBUG mode set
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
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
