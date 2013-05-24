from mysite.views.view_functions import response
from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from blog.models import Post, Link


# Blog page view
def blog(request):
    errors = []
    posts = Post.objects.all()
    links = []
    choices = Link.objects.values_list('category', flat=True).distinct()
    for choice in choices:
        for link in Link.objects.filter(category=choice)
            links.append(link)
    template = 'blog.html'
    context = {
        'errors': errors,
        'choices': choices,
        'posts': posts,
        'links': links,
    }
    return response(request, template, context)


def post_detail(request, post_id):
    errors = []
    post = Post.objects.get(id=post_id)
    links = Link.objects.all()
    template = 'post_detail.html'
    context = {
        'errors': errors,
        'post': post,
        'links': links,
    }
    return response(request, template, context)
