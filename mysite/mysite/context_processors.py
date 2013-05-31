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
        'SITE_YEARS': site_years,
        # Base
        'HOME_URL': '/home/',
        'BLOG_URL': '/blog/',
        'PORTFOLIO_URL': '/portfolio/',
        'ABOUTME_URL': '/aboutme/',
        'MFF_URL': '/mff/',
    }
    return context
