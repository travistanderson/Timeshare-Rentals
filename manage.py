#!/usr/bin/env python

import sys

sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages")
sys.path.insert(0, "/Library/Python/2.6/site-packages")
sys.path.insert(0, "/Users/travis/Dropbox/webs_travis/dev_timesharerentals/timeshare/apps")
sys.path.insert(0, "/home/travis/timesharerentals.com/timeshare/apps")
sys.path.insert(0, "/Users/annie/Dropbox/tsr/timeshare/apps")

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)




