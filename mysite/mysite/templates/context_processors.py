# $Id: context_processors.py,v 1.5 2013-04-02 01:36:27-07 dmfrank - $
# -*- coding: utf-8 -*-
# Global template variables populated with context_processors.

def global_vars(request):
  context = {
    # Site specific
    'SITENAME': 'derekmfrank',
    'SITENAME_': 'DerekMFrank',
    'SITEURL': 'derekmfrank.com',
    'SITE_URL': 'derekmfrank.com',
    # Static content urls
    'JS_URL': '/static/js/',
    'IMG_URL': '/static/img/',
    'CSS_URL': '/static/css/',
    # Base
    'HOME_URL': '/home/',
    'BLOG_URL': '/blog/',
    'PORTFOLIO_URL': '/portfolio/',
    'ABOUTME_URL': '/aboutme/',
    'MFF_URL': '/mff/',
  }
  return context
