# -*- coding: utf-8 -*-
# $Id: context_processors.py,v 1.5 2013-05-30 19:34:20-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   context_processors.py
#
# DESCRIPTION
#   Global template variables populated with context_processors.
#

import datetime
from aboutme.views import get_me

def site(request):
    site_years = '2013'
    year = str(datetime.date.today().year)
    if year != site_years:
        site_years = site_years + '-' + year

    context = {
        # Me
        'me': get_me(),
        # Site specific
        'SITENAME': 'derekmfrank',
        'SITENAME_': 'Derek M. Frank',
        'SITEURL': 'derekmfrank.com',
        'SITE_URL': 'derekmfrank.com',
        'SITE_YEARS': site_years,
        # Me sspecific
        'GMAIL': 'derekmfrank@gmail.com',
        'GMX': 'dmfrank@gmx.com',
        #'RESUME_LINK': '/static/doc/dmfrank-resume.pdf',
        'RESUME_LINK_PDF': 'https://docs.google.com/file/d/0B0oohzBQeJoFeGgzYnRoMkZGSW8/edit?usp=sharing',
        'RESUME_LINK_DOCX': 'https://docs.google.com/file/d/0B0oohzBQeJoFMFRBSUxmbUZfdlk/edit?usp=sharing',
        'GITHUB_URL': 'https://github.com/dmfrank/',
        'BITBUCKET_URL': 'https://bitbucket.org/dmfrank/',
        #'STACKEXCHANGE_URL': 'https://stackexchange.com/users/1076669/dmfrank',
        'STACKEXCHANGE_URL': 'https://stackexchange.com/users/1076669',
        'BEYOND_URL': 'http://www.beyond.com/_dmf_',
        #'LINKEDIN_URL': 'https://www.linkedin.com/pub/derek-frank/40/868/328',
        'LINKEDIN_URL': 'https://www.linkedin.com/in/derekmfrank',
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
