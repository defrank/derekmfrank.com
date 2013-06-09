# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - blog
#
# DESCRIPTION
#   Views for blogs.
#
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as Owner

from utils.functions import response
from models import CATEGORY_CHOICES, Post, Link


####
## VIEWS

def blog_view(request, template, context):
    """All blog views: contain links menu"""
    #choices = Link.objects.values_list('category', flat=True).distinct()
    categories = CATEGORY_CHOICES
    sources = []
    for c in categories:
        links = Link.objects.filter(category=c[0]).order_by('timestamp').reverse()
        if links:
            sources.append((c[-1], links))

    context['sources'] = sources
    return response(request, template, context)
    

def recent(request):
    """Blog homepage: view eight most recent posts."""
    posts = Post.objects.order_by('timestamp').reverse()[8:]

    template = 'blog/posts.html'
    context = {
        'posts': posts,
    }
    return blog_view(request, template, context)


## Indices
def index(request):
    """Archive index by post date."""
    #filters = ('user', 'year', 'month', 'day')
    # Retrieve index list of year/month/day
    index =  Post.objects.filter(draft=False).dates('timestamp', 'day', order='DESC')

    template = 'blog/index.html'
    context = {
        'index': index,
    }
    return blog_view(request, template, context)


## Archives:
def archive_view(request, posts):
    """
    All archive views: contain posts.
    
    Takes a list of blog posts.
    """
    template = 'blog/posts.html'
    context = {
        'posts': posts,
    }
    return blog_view(request, template, context)


def archive_user(request, username):
    """
    Archive: view by user.

    Takes a user's username.
    """
    user = Owner.objects.get(username=username)
    posts = Post.objects.filter(owner=user).order_by('timestamp')
    return archive_view(request, posts)


def archive_id(request, post_id):
    """
    Archive: view by id.

    Takes an integer specifying the post id.
    """
    post = get_object_or_404(Post, id=post_id)
    return archive_view(request, post)

   
def archive_year(request, year):
    """
    Archive: view by year.
    
    Takes an integer specifying the posting year.
    """
    # Retrieve year list of dates that have posts (descending order)
    posts = Post.objects.filter(timestamp__year=year).order_by('timestamp').reverse()
    return archive_view(request, posts)


def archive_month(request, year, month):
    """
    Archive: view by year/month.
    
    Takes two integers specifying year and month.
    """
    # Retrieve year/month list of dates that have posts (descending order)
    posts = Post.objects.filter(timestamp__year=year, timestamp__month=month).order_by('timestamp').reverse()
    return archive_view(request, posts)


def archive_day(request, year, month, day):
    """
    Archive: view by year/month/day.
    
    Takes three integers specifying year, month, and day.
    """
    # Retrieve year/month list of dates that have posts (descending order)
    posts = Post.objects.filter(timestamp__year=year, timestamp__month=month, timestamp__day=day).order_by('timestamp').reverse()
    return archive_view(request, posts)
