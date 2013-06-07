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
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

import markdown


####
## HELPERS

def default_owner():
    """Function to return the first User from the database."""
    return User.objects.get(id=1)


def markdown_to_html(markdownText, images):
    """Function to parse and add image in html format to a blog post"""
    # create instance of Markdown class
    md = markdown.Markdown()
    for image in images:
        if image.image:
            image_url = settings.STATIC_URL + image.image.url
        elif image.url:
            image_url = image.url
        # append image reference to Markdown instance
        # md.reference[id] = (url, title)
        md.reference[image.title] = (image_url, '%s' % image.title)
    # parse source text
    return md.convert(markdownText)


####
## MODELS

## Post Model:
class Post(models.Model):
    """
    A blog post.

    Owner, title, and body are required. Other fields optional.
    """
    owner = models.ForeignKey(User, default=default_owner())
    title = models.CharField(_(u'post title'), max_length=128)
    timestamp = models.DateTimeField(_(u'post date and time'), auto_now_add=True)
    body = models.TextField(_(u'post body'))

    def body_html(self):
        return markdown_to_html(self.body, self.image_set.all())

    def Meta(self):
        ordering = ['-timestamp']
    
    def __unicode__(self):
        return self.title


class PostImage(models.Model):
    """
    A blog post's image.

    Post and either the image or url field are required. Other fields optional.
    """
    post = models.ForeignKey(Post)
    title = models.CharField(_(u'image title'), max_length=64, unique=True, blank=True)
    def get_upload_dir(instance, filename):
        return 'blog/%s/post%d/%s' % (instance.owner.username, instance.id, filename)
    image = models.ImageField(_(u'upload post image'), upload_to=get_upload_dir, blank=True)
    url = models.URLField(_(u'post image link'), blank=True)

    def Meta(self):
        ordering = ['-post', 'title']

    def __unicode__(self):
        if self.title:
            return self.title 
        elif self.image:
            return self.image.url
        elif self.url:
            return self.url
        return 'image for ' + self.post


## Link Model:
CATEGORY_CHOICES = (
    (u'CO', u'Cosmos'),
    (u'TC', u'Technology'),
    (u'LH', u'Life Hacks'),
    (u'PO', u'Politics'),
    (u'OT', u'Other'),
)
class Link(models.Model):
    """
    A link to something of interest.

    All fields required.
    """
    owner = models.ForeignKey(User, default=default_owner())
    title = models.CharField(_(u'link title'), max_length=128)
    timestamp = models.DateTimeField(_(u'link date and time'), auto_add_now=True)
    url = models.URLField(_(u'link address'))
    category = models.CharField(_(u'link category'), max_length=2, choices=CATEGORY_CHOICES, default=u'OT')

    def Meta(self):
        ordering = ['category', '-timestamp', 'title']

    def __unicode__(self):
        return self.title


####
## ADMIN

## Post
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 2

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'get_owner')
    fieldsets = [
        (None, {'fields': ['owner']}),
        ('Post information', {'fields': ['title', 'timestamp']}),
        ('Post content', {'fields': ['body']}),
    ]
    inlines = [PostImageInline]

    def get_owner(self, obj):
        return '%s' % obj.owner.get_profile()
    get_owner.short_description = u'Owner'


## Link
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'timestamp', 'get_owner')

    def get_owner(self, obj):
        return '%s' % obj.owner.get_profile()
    get_owner.short_description = u'Owner'


####
## REGISTER
admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)
