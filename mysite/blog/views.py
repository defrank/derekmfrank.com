from mysite.views.view_functions import response
from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from blog.models import CATEGORY_CHOICES, Post, Link


# Blog page view
def blog(request):
    errors = []
    posts = Post.objects.order_by('timestamp').reverse()
    links = Link.objects.order_by('timestamp').reverse()
    #choices = Link.objects.values_list('category', flat=True).distinct()
    template = 'blog.html'
    context = {
        'errors': errors,
        #'choices': choices,
        'categories': CATEGORY_CHOICES,
        'posts': posts,
        'links': links,
    }
    return response(request, template, context)


def post_detail(request, post_id):
    errors = []
    post = Post.objects.get(id=post_id)
    links = Link.objects.order_by('timestamp').reverse()
    template = 'post_detail.html'
    context = {
        'errors': errors,
        'categories': CATEGORY_CHOICES,
        'post': post,
        'links': links,
    }
    return response(request, template, context)
