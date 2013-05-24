from mysite.views.view_functions import response
from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from blog.models import Post, Link


# Blog page view
def blog(request):
    errors = []
    choices = []
    posts = Post.objects.all()
    links = Link.objects.all()
    for link in links:
        choices.append(link.category)
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
    template = 'post.html'
    context = {
        'errors': errors,
        'post' = post,
    }
    return response(request, template, context)
