# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - blog
#
# DESCRIPTION
#   Models definition for mysite blog.
#

from django.db import models
from django.contrib import admin

from aboutme.models import Person
from aboutme.views import get_me


## BLOG

CATEGORY_CHOICES = (
    (u'CO', u'Cosmos'),
    (u'TC', u'Technology'),
    (u'LH', u'Life Hacks'),
    (u'PO', u'Politics'),
    (u'OT', u'Other'),
)

# Post
class Post(models.Model):
    owner = models.ForeignKey(Person, null=True, default=get_me())
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="blog/img/")
    image_url = models.URLField(blank=True, verify_exists=True, null=True)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

# Link
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(verify_exists=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=u'OT')
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title


## BLOG ADMIN

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'timestamp')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'timestamp')


## ADMIN REGISTER
admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)
