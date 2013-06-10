# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
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
    projects = Project.objects.filter(author=author)
    education = Education.objects.filter(author=author)
    #departments = Education.DEPARTMENT_CHOICES
    departments = Course.objects.values_list('department').distinct()
    """
    for i in institutions:
        dept_courses = []
        for d in departments:
            courses = Course.objects.filter(department=d[0])
            course_asgs = []
            if courses:
                for c in courses:
                    asgs = Assignment.objects.filter(course=c).order_by('identification')
                    course_asgs.append((c, asgs))
            if course_asgs:
                dept_courses.append((d[-1], course_asgs))
        education.append((i, dept_courses))
    """

    context = {
        'author': author,
        'projects': projects,
        'education': education,
        'departments': departments,
    }
    return portfolio_views(request, context, author)


def someone(request, username):
    """Takes a username value"""
    author = User.objects.get(username=username)
    context = {
        'author': author,
    }
    return response(request, template, context)
