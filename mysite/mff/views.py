# $Id: views.py,v 1.4 2013-05-27 12:40:43-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   views.py - mff
#
# DESCRIPTION
#   A template views definition for MFF.
#

from django.conf import settings
from django.contrib.sites.models import get_current_site

from utils.functions import response
from models import Source, Information, Topic, TopicListBit

# MFF page view
def mff(request):
    errors = []
    topics = []
    alltopics = Topic.objects.all()
    for topic in alltopics:
        bits = TopicListBit.objects.filter(topic=topic)
        topics.append((topic, bits))
    mff = Information.objects.get(id=1)
    template = 'mff.html'
    context = {
        'errors': errors,
        'topics': topics,
        'mff': mff,
    }
    return response(request, template, context)
