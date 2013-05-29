from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from utils.functions import response
from mysite.models import DEPARTMENT_CHOICES
from aboutme.models import Source
from models import Project, Education, Course, Assignment


# Portfolio page view
def portfolio(request):
    errors = []
    sources = Source.objects.order_by('priority', 'type', 'title' )
    projects = Project.objects.order_by('date').reverse()
    education = []
    institution = Education.objects.order_by('graduation_date').reverse()
    for i in institution:
        courses = Course.objects.order_by('department', 'number').reverse()
        course_asg = []
        for c in courses:
            asgs = Assignment.objects.filter(course=c).order_by('identification')
            course_asg.append([c, asgs])
        education.append([i, course_asg])
    department_list = Course.objects.values_list('department').distinct()
    departments = []
    for d in department_list:
        #departments.append(d)
        for c in DEPARTMENT_CHOICES:
            if d == c[0]:
                departments.append(c)
            
    template = 'portfolio.html'
    context = {
        'errors': errors,
        'sources': sources,
        'projects': projects,
        'education': education,
        'departments': DEPARTMENT_CHOICES,
        #'departments': departments,
    }
    return response(request, template, context)
