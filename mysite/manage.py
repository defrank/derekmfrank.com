#!/usr/bin/env python2.6
# $Id: manage.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   manage.py
#

import os, sys
from django.core.management import execute_manager
#try:
    #import settings # Assumed to be in the same directory.
#except ImportError:
    #import sys
    #sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    #sys.exit(1)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    #execute_manager(settings)
