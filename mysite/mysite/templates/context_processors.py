# $Id: context_processors.py,v 1.5 2013-04-02 01:36:27-07 dmfrank - $
# -*- coding: utf-8 -*-
# Global template variables populated with context_processors.

def global_vars(request):
  context = {
    # Site specific
    'SITENAME': 'trumur',
    'SITENAME_': 'Trumur',
    'SITEURL': 'trumur.com',
    'SITE_URL': 'trumur.com',
    # Static content urls
    'JS_URL': '/static/js/',
    'IMG_URL': '/static/img/',
    'CSS_URL': '/static/css/',
    # Account urls: settings, login, logout
    'ACCOUNT_URL': '/accounts/',
    'SETTINGS_URL': '/accounts/settings/',
    'LOGIN_URL': '/accounts/login/',
    'LOGOUT_URL': '/accounts/logout/',
    # Base
    'HOME_URL': '/home/',
    'SEARCH_URL': '/search/',
    #'SEARCH_URL': 'http://www.google.com/search',
    'NOTIFICATION_URL': '/notifications/',
    'PROFILE_URL': '/profile/',
    'FRIENDS_URL': '/friends/',
    'POINTS_URL': '/points/',
    'HISTORY_URL': '/history/',
    # Testing/temp
    'honesty_points': '1 ',
    'caliber_points': ' 10',
  }
  return context
