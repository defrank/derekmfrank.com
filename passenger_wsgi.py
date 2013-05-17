# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   passenger_wsgi.py
#
# DESCRIPTION
#   Wsgi script required by Dreamhost for Passenger.
#
import sys, os

cwd = os.path.abspath(os.path.dirname(__file__))
myapp_directory = cwd + '/mysite'
sys.stdout = sys.stderr
sys.path.insert(0,myapp_directory)

if cwd not in sys.path:
    sys.path.append(cwd)
project = os.path.join(cwd, 'mysite').replace('\\','/')
if project not in sys.path:
    sys.path.append(project)
myproject = os.path.join(cwd, 'mysite', 'mysite').replace('\\','/')
#if myproject not in sys.path:
    #sys.path.append(myproject)

if sys.version < "2.4": os.execl("/usr/bin/python2.4", "python2.4", *sys.argv)

#os.environ['PYTHON_EGG_CACHE'] = os.path.join(os.environ['HOME'], 'tmp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from paste.exceptions.errormiddleware import ErrorMiddleware
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# To cut django out of the loop, comment the above application = ... line ,
# and remove "test" from the below function definition.
def testapplication(environ, start_response):
    status = '200 OK'
    output = 'Hello World! Running Python version ' + sys.version + '\n\n'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    # to test paste's error catching prowess, uncomment the following line
    # while this function is the "application"
    #raise("error")
    start_response(status, response_headers)
    return [output]

#def application(environ, start_response):
    #start_response('200 OK', [('Content-type', 'text/plain')])
    #return ["Hello, world!"]

application = ErrorMiddleware(application, debug=True)
