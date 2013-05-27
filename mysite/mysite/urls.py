# $Id: urls.py,v 1.4 2013-05-27 12:40:43-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   urls.py - mysite
#
# DESCRIPTION
#   A url patterns definition for mysite derekmfrank.com.
#

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.views.static import serve as views_static_serve
from mysite.views import view_functions, views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Base Views
    url(r'^$', views.home, name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^mff/$', views.mff, name='mff'),

    # Media
    url(r'^static/(?P<path>.*)$', views_static_serve, { 'document_root': settings.STATIC_ROOT, }),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Media files serve only with DEBUG mode set
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PHP MySQL Database
urlpatterns += patterns('',
    url(r'^dh_phpmyadmin.*$', view_functions.redirect_to_mysql, name='mysql'),
    url(r'^mysql.*$', view_functions.redirect_to_mysql, name='mysql'),
)

# Webmasters and other 3rd party apps
urlpatterns += patterns('',
    url(r'^', include('webmaster.urls')),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', view_functions.redirect_to_home, name='redirect'),
)
