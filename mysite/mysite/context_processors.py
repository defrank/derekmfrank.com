# -*- coding: utf-8 -*-
# $Id: context_processors.py,v 1.1 2013-04-19 14:12:27-07 dmfrank - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   context_processors.py
#
# DESCRIPTION
#   Global template variables populated with context_processors.
#

import datetime

def site(request):
    site_years = '2013'
    year = str(datetime.date.today().year)
    if year != site_years:
        site_years = site_years + '-' + year

    context = {
        # Site specific
        'SITENAME': 'derekmfrank',
        'SITENAME_': 'Derek M. Frank',
        'SITEURL': 'derekmfrank.com',
        'SITE_URL': 'derekmfrank.com',
        'SITE_YEARS': site_years,
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
