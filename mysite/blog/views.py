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
from django.contrib.auth.models import User

from utils import response
from models import Entry, Link


####
## VIEWS

def blog_view(request, template, context):
    """All blog views: contain links menu"""
    #choices = Link.objects.values_list('category', flat=True).distinct()
    categories = Link.CATEGORY_CHOICES
    sources = []
    for c in categories:
        links = Link.objects.filter(category=c[0]).order_by('timestamp').reverse()
        if links:
            sources.append((c[-1], links))

    context['sources'] = sources
    return response(request, template, context)
    

def recent(request):
    """Blog homepage: view eight most recent posts/entries."""
    entries = Entry.objects.order_by('timestamp').reverse()

    template = 'blog/entries.html'
    context = {
        'entries': entries,
    }
    return blog_view(request, template, context)


## Indices
def index(request):
    """Archive index by post date."""
    #filters = ('user', 'year', 'month', 'day')
    # Retrieve index list of year/month/day
    index =  Entry.objects.filter(draft=False).dates('timestamp', 'day', order='DESC')

    template = 'blog/index.html'
    context = {
        'index': index,
    }
    return blog_view(request, template, context)


## Archives:
def archive_view(request, entries):
    """
    All archive views: contain blog entries.
    
    Takes a list of blog entries.
    """
    template = 'blog/entries.html'
    context = {
        'entries': entries,
    }
    return blog_view(request, template, context)


def archive_author(request, username):
    """
    Archive: view by user author.

    Takes a user's username.
    """
    user = User.objects.get(username=username)
    entries = Entry.objects.filter(author=user).order_by('timestamp')
    return archive_view(request, entries)


def archive_id(request, entry_id):
    """
    Archive: view by id.

    Takes an integer specifying the entry id.
    """
    entry = get_object_or_404(Entry, id=entry_id)
    return archive_view(request, entry)

   
def archive_year(request, year):
    """
    Archive: view by year.
    
    Takes an integer specifying the posting year.
    """
    # Retrieve year list of dates that have entries (descending order)
    entrie = Entry.objects.filter(timestamp__year=year).order_by('timestamp').reverse()
    return archive_view(request, entries)


def archive_month(request, year, month):
    """
    Archive: view by year/month.
    
    Takes two integers specifying year and month.
    """
    # Retrieve year/month list of dates that have entries (descending order)
    entries = Entry.objects.filter(timestamp__year=year, timestamp__month=month).order_by('timestamp').reverse()
    return archive_view(request, entries)


def archive_day(request, year, month, day):
    """
    Archive: view by year/month/day.
    
    Takes three integers specifying year, month, and day.
    """
    # Retrieve year/month list of dates that have entries (descending order)
    entries = Entry.objects.filter(timestamp__year=year, timestamp__month=month, timestamp__day=day).order_by('timestamp').reverse()
    return archive_view(request, entries)
