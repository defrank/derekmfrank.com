from mysite.views.view_functions import response
from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from portfolio.models import DEPARTMENT_CHOICES, Education, Course, Assignment


# Portfolio page view
def portfolio(request):
    errors = []
    education = []
    institution = Education.objects.order_by('graduation_date').reverse()
    for i in institution:
        courses = Course.objects.order_by('department', 'number')
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
        'education': education,
        'departments': DEPARTMENT_CHOICES,
        #'departments': departments,
    }
    return response(request, template, context)
