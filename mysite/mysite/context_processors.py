# -*- coding: utf-8 -*-
# $Id: context_processors.py,v 1.6 2013-05-30 23:30:49-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   context_processors.py
#
# DESCRIPTION
#   Global template variables populated with context_processors.
#

import datetime
from utils.functions import get_default_user

def site(request):
    site_years = '2013'
    year = str(datetime.date.today().year)
    if year != site_years:
        site_years = site_years + '-' + year

    context = {
        # Me
        'me': get_default_user,
        # Site specific
        'SITE_YEARS': site_years,
        # Base
    }
    return context
