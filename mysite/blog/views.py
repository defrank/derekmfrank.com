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
    # Sources
    choices = Link.objects.values_list('category', flat=True).distinct()
    categories = [ (c, C) for c,C in Link.CATEGORY_CHOICES if c in choices ]
    sources = [ (category[-1], Link.objects.filter(category=category[0])) for category in categories ]

    # Previous entries
    previous = Entry.objects.all()[:16]

    # Dates archive
    dates = Entry.objects.values_list('timestamp', flat=True).distinct()
    dates_index = list(set([ date.year for date in set(dates) ]))
    for y in range(len(dates_index)):
        months = list(set([ date.month for date in dates if date.year == dates_index[y] ]))
        for m in range(len(months)):
            days = list(set([ date.day for date in dates if date.year == dates_index[y] and date.month == months[m] ]))
            months[m]= (months[m], days)
        dates_index[y] = (dates_index[y], months)

    # Author archive
    ids = list(set(Entry.objects.values_list('author', flat=True).distinct()))
    authors_index = [ User.objects.get(pk=id) for id in ids ]
            
    context['sources'] = sources
    context['previous'] = previous
    context['authors'] = authors_index
    context['dates'] = dates_index
    return response(request, template, context)
    

def blog(request):
    """
    All blog entries.
    """
    entries = Entry.objects.all()

    template = 'blog/blog.html'
    context = {
        'entries': entries,
    }
    return blog_view(request, template, context)


def recent(request):
    """Blog homepage: view eight most recent posts/entries."""
    entries = Entry.objects.all()[:8]

    template = 'blog/recent.html'
    context = {
        'entries': entries,
    }
    return blog_view(request, template, context)


## Archives:
def archive_view(request, entries):
    """
    All archive views: contain blog entries.
    
    Takes a list of blog entries.
    """
    template = 'blog/blog.html'
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
    entries = Entry.objects.filter(author=user)
    return archive_view(request, entries)


def archive_id(request, id):
    """
    Archive: view by id.

    Takes an integer specifying the entry id.
    """
    entry = (get_object_or_404(Entry, id=id), )
    return archive_view(request, entry)

   
def archive_year(request, year):
    """
    Archive: view by year.
    
    Takes an integer specifying the posting year.
    """
    # Retrieve year list of dates that have entries (descending order)
    entries = Entry.objects.filter(timestamp__year=year)
    return archive_view(request, entries)


def archive_month(request, year, month):
    """
    Archive: view by year/month.
    
    Takes two integers specifying year and month.
    """
    # Retrieve year/month list of dates that have entries (descending order)
    entries = Entry.objects.filter(timestamp__year=year, timestamp__month=month)
    return archive_view(request, entries)


def archive_day(request, year, month, day):
    """
    Archive: view by year/month/day.
    
    Takes three integers specifying year, month, and day.
    """
    # Retrieve year/month list of dates that have entries (descending order)
    entries = Entry.objects.filter(timestamp__year=year, timestamp__month=month, timestamp__day=day)
    return archive_view(request, entries)
