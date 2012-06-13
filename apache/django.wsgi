import os
import sys

path2 = "/root/www/html/jjshop"
if path2 not in sys.path:
	sys.path.append(path2)

path1 = "/root/www/html"
if path1 not in sys.path:
	sys.path.append(path1)

path3 = "/root/www"
if path3 not in sys.path:
	sys.path.append(path3)

os.environ['DJANGO_SETTINGS_MODULE'] = 'jjshop.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
