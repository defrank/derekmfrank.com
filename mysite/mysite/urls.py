from django.conf.urls.defaults import patterns, include, url
from views import view_functions, views, account_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Google Analytics/Webmaster
    url(r'^google0a2e75908547fa0e.html$', views.webmaster, name='webmaster'),

    # Accounts: login, logout, settings
    #url(r'^accounts/$', account_views.account, name='account'),
    #url(r'^accounts/login/$', account_views.login, name='login'),
    #url(r'^accounts/logout/$', account_views.logout, name='logout'),
    #url(r'^accounts/logged_out/$', account_views.logged_out, name='logged_out'),
    # Settings
    #url(r'^accounts/settings/$', account_views.settings, name='settings'),

    # Necessary redirection
    url(r'^accounts/profile/$', view_functions.redirect_to_home, name='home'),

    # Base Views
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^points/$', views.points, name='points'),
    url(r'^history/$', views.history, name='history'),
    url(r'^profile/$', views.profile, name='profile'),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
