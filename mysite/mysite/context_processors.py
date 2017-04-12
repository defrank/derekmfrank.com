# -*- coding: utf-8 -*-
# $Id: context_processors.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank
#
# NAME
#   context_processors.py
#
# DESCRIPTION
#   Global template variables populated with context_processors.
#

import datetime
from utils import get_default_user as _user

def site(request):
    site_years = '2013'
    year = str(datetime.date.today().year)
    if year != site_years:
        site_years = site_years + '-' + year

    context = {
        # Me
        'me': _user,
        # Site specific
        'SITE_YEARS': site_years,
        # Base
    }
    return context
