# $Id: $
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


## BLOG

CATEGORY_CHOICES = (
    ('CO', 'Cosmos'),
    ('TC', 'Technology'),
    ('CS', 'Computer Science'),
    ('PO', 'Politics'),
)

# Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, verify_exists=True)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

# Link
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(verify_exists=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title


## BLOG ADMIN

class PostAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'title')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'title')


## ADMIN REGISTER

admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)
