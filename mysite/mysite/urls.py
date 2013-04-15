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
    # Google Analytics/Webmaster
    url(r'^google0a2e75908547fa0e.html$', views.webmaster, name='webmaster'),

    # Base Views
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='homepage'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^mff/$', views.mff, name='mff'),

    # Media
    url(r'^static/(?P<path>.*)$', views_static_serve, { 'document_root': settings.STATIC_ROOT, }),

    # Necessary redirection
    url(r'^accounts/profile/$', view_functions.redirect_to_home),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
