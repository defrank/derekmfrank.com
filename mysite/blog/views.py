from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from utils.functions import response
from models import CATEGORY_CHOICES, Post, Link


# Get Sources
def get_sources():
    #choices = Link.objects.values_list('category', flat=True).distinct()
    categories = CATEGORY_CHOICES
    sources = []
    for c in categories:
        links = Link.objects.filter(category=c[0]).order_by('timestamp').reverse()
        if links:
            sources.append((c[-1], links))
    return sources


# Blog page view
def blog(request):
    errors = []
    posts = Post.objects.order_by('timestamp').reverse()
    sources = get_sources()
    template = 'blog.html'
    context = {
        'errors': errors,
        'posts': posts,
        'sources': sources,
    }
    return response(request, template, context)


def post_detail(request, post_id):
    errors = []
    post = Post.objects.get(id=post_id)
    if not post:
        return blog(request)
    sources = get_sources()
    template = 'post_detail.html'
    context = {
        'errors': errors,
        'post': post,
        'sources': sources,
    }
    return response(request, template, context)
