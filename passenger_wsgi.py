import sys, os

cwd = os.getcwd()
myapp_directory = cwd + '/mysite/apps'
sys.stdout = sys.stderr
sys.path.insert(0,myapp_directory)
sys.path.append(cwd)
sys.path.append(os.path.join(cwd, 'mysite').replace('\\','/'))

if sys.version < "2.4": os.execl("/usr/bin/python2.4", "python2.4", *sys.argv)
#sys.path.insert(1, os.path.join(os.getenv('HOME'), 'django/source').replace('\\','/'))
#sys.path.insert(1, os.path.join(os.getenv('HOME'), 'django/applications').replace('\\','/'))
#sys.path.insert(1, os.path.join(os.getenv('HOME'), 'django/projects').replace('\\','/'))
os.environ['DJANGO_SETTINGS_MODULE'] = "mysite.settings"

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
application = ErrorMiddleware(application, debug=True)
