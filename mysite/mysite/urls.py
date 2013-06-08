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
)

urlpatterns += patterns('',
    url(r'^about/', include('limn.urls')),
    url(r'^portfolio/', include('porject.urls')),
    url(r'^blog/', include('blog.urls')),
    #url(r'^mff/', include('mff.urls')),

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
urlpatterns += patterns('utils.functions',
    url(r'^dh_phpmyadmin.*$', 'redirect_to_mysql', name='mysql'),
    url(r'^mysql.*$', 'redirect_to_mysql'),
)

# Webmasters and other 3rd party apps
urlpatterns += patterns('',
    url(r'^', include('webmaster.urls')),
)

# Necessary redirection for unavailable pages
#urlpatterns += patterns('',
    #url(r'^.+$', functions.redirect_to_home, name='redirect'),
#)
