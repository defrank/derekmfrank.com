# $Id: context_processors.py,v 1.5 2013-04-02 01:36:27-07 dmfrank - $
# -*- coding: utf-8 -*-
# Global template variables populated with context_processors.

def global_vars(request):
  context = {
    # Site specific
    'SITENAME': 'derekmfrank',
    'SITENAME_': 'Derek M. Frank',
    'SITEURL': 'derekmfrank.com',
    'SITE_URL': 'derekmfrank.com',
    # Me sspecific
    'RESUME_LINK': '/static/doc/dmfrank-resume.pdf',
    'GITHUB_URL': 'https://github.com/dmfrank/',
    'BITBUCKET_URL': 'https://bitbucket.org/dmfrank/',
    'LINKEDIN_URL': 'https://www.linkedin.com/pub/derek-frank/40/868/328',
    'FLAVORSME_URL': 'http://flavors.me/derekmfrank/',
    # Static content urls
    'JS_URL': '/static/js/',
    'IMG_URL': '/static/img/',
    'CSS_URL': '/static/css/',
    'DOC_URL': '/static/doc/',
    # Base
    'HOME_URL': '/home/',
    'BLOG_URL': '/blog/',
    'PORTFOLIO_URL': '/portfolio/',
    'ABOUTME_URL': '/aboutme/',
    'MFF_URL': '/mff/',
  }
  return context
