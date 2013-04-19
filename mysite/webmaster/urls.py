from django.conf.urls import patterns, url
from webmaster import views


# Webmasters and other 3rd party site apps
urlpatterns = patterns('',
    # Google Analytics/Webmaster
    url(r'^google0a2e75908547fa0e.html$', views.google, name='googlewebmaster'),
    
    # Bing Webmaster
    url(r'^BingSiteAuth.xml$', views.bing, name='bingwebmaster'),
)
