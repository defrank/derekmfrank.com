from mysite.views.view_functions import response
from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

#from portfolio.models import Project, Education


# Portfolio page view
def portfolio(request):
    errors = []
    template = 'portfolio.html'
    context = {
        'errors': errors,
    }
    return response(request, template, context)
