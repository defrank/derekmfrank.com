# $Id: views.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - portfolio
#
# DESCRIPTION
#   Views for portfolio.
#
from django.conf import settings
from django.contrib.auth.models import User

from utils import response, get_default_user as _user

from models import Project, Education, Course


####
## VIEWS

## Portfolio:
def portfolio_views(request, context, author):
    """
    Portfolio view: has sources

    Takes a context and User.
    """
    authors = Project.objects.values_list('author', flat=True).distinct()

    template = 'portfolio/portfolio.html'
    context['authors'] = authors
    return response(request, template, context)


def portfolio(request):
    """Outputs the default user's portfolio"""
    author = _user

    # Projects
    projects = Project.objects.filter(author=author)

    # Education
    education = Education.objects.filter(author=author)
        # Departments
    choices = Course.objects.values_list('department', flat=True).distinct()
    departments = [ (d, D) for d,D in Education.DEPARTMENT_CHOICES if d in choices ]

    context = {
        'myuser': author,
        'projects': projects,
        'education': education,
        'departments': departments,
    }
    return portfolio_views(request, context, author)


def user(request, username):
    """Takes a username value"""
    author = User.objects.get(username=username)
    context = {
        'author': author,
    }
    return response(request, template, context)
