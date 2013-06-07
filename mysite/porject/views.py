from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.contrib.auth.models import User

from utils.functions import response

from limn.models import UserSource as Source, UserProfileSource as Profile, UserRepositorySource as Repo

from models import Project, Education
from models import DEPARTMENT_CHOICES


####
## HELPERS

def get_default_user():
    return User.objects.get(id=1)


####
## VIEWS

## Portfolio:
def portfolio_views(request, context, user):
    """
    Portfolio view: has sources

    Takes a context and User.
    """
    sources = []
    repos = Repo.objects.filter(user=profile)
    sources.append(repos)
    profiles = Profile.objects.filter(user=profile)
    sources.append(profiles)
    owners = Project.objects.values_list('owner', flat=True).distinct()

    template = 'portfolio/portfolio.html'
    context['sources'] = sources
    context['owners'] = owners
    return response(request, template, context)

def portfolio(request):
    """Outputs the default user's portfolio"""
    owner = get_default_user()
    projects = Project.objects.filter(user=owner)
    education = []
    departments = DEPARTMENT_CHOICES
    institution = Education.objects
    for i in institution:
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

    context = {
        'owner': owner,
        'projects': projects,
        'education': education,
    }
    return response(request, template, context)


def someone(request, username):
    """Takes a username value"""
    owner = User.objects.get(username=username)
    context = {
        'owner': owner,
    }
    return response(request, template, context)
