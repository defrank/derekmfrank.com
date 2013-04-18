from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.views.static import serve as views_static_serve
from mysite.views import view_functions, views
#from mysite.settings import STATIC_ROOT

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Base Views
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^mff/$', views.mff, name='mff'),

    # Media
    url(r'^static/(?P<path>.*)$', views_static_serve, { 'document_root': settings.STATIC_ROOT, }),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

# Media files serve only with DEBUG mode set
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# PHP MySQL Database
urlpatterns += patterns('',
    url(r'^dh_phpmyadmin.*$', view_functions.redirect_to_mysql, name='mysql'),
    url(r'^mysql.*$', view_functions.redirect_to_mysql, name='mysql'),
)

# Google apps specific urls
urlpatterns += patterns('',
    # Google Analytics/Webmaster
    url(r'^google0a2e75908547fa0e.html$', views.webmaster, name='webmaster'),
)

# Necessary redirection for unavailable pages
urlpatterns += patterns('',
    url(r'^.+$', view_functions.redirect_to_home, name='redirect'),
)
