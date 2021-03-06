# $Id: models.py,v 1.1 2013-06-30 17:08:56-07 dmf - $
# Derek Frank
#
# NAME
#   models.py - blog
#
# DESCRIPTION
#   Models definition for mysite blog.
#

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from os.path import basename, splitext
from urlparse import urlsplit

from utils import get_default_user as _user, markdown_to_html


####
## MODELS

class Entry(models.Model):
    """
    A blog post entry.

    Author, title, and body are required. Other fields optional.
    """
    author = models.ForeignKey(User, related_name='entries', default=_user)
    title = models.CharField(_(u'title'), max_length=128)
    timestamp = models.DateTimeField(_(u'entry date and time'))
    html = models.BooleanField(_('html in body?'))
    body = models.TextField(_(u'body text'))

    def body_html(self):
        if self.html:
            images = self.images.all()
            return markdown_to_html(self.body, images)
        return self.body

    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.archive_id', [str(self.id)])
   
    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('-timestamp', 'author', 'title')
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
 

class Image(models.Model):
    """
    A blog post's image.

    Entry and either the image or url field are required. Other fields optional.
    """
    entry = models.ForeignKey(Entry, related_name='images')
    title = models.CharField(_(u'title'), max_length=64, blank=True)
    def get_upload_dir(instance, filename):
        return 'blog/%s/entry%d/%s' % (instance.entry.author.username, instance.entry.pk, filename)
    image = models.ImageField(_(u'uploaded image'), upload_to=get_upload_dir, blank=True, null=True)
    url = models.URLField(_(u'url address'), blank=True)

    def filename(self):
        if self.title:
            return self.title
        elif self.image:
            return basename(self.image.url)
        elif self.url:
            return basename(urlsplit(self.url).path)
        return 'image%d' % self.id

    def get_absolute_url(self):
        if self.image:
            return '%s' % self.image.url
        elif self.url:
            return '%s' % self.url
        return ''

    def __unicode__(self):
        if self.image:
            name = basename(self.image.path)
            if self.title:
                return u'%s%s' % (self.title, splitext(name)[-1])
            return u'%s' % name
        elif self.url:
            name = urlsplit(self.url).netloc
            if self.title:
                return u'%s (hosted on %s)' % (self.url, name)
            return u'unknown (hosted on %s)' % name
        elif self.title:
            return u'%s' % self.title
        return u'image %d for blog entry %d: %s' % (self.id, self.entry.id, self.entry)

    class Meta:
        ordering = ('-entry', 'title')


class Link(models.Model):
    """
    A link to something of interest.

    All fields required.
    """
    author = models.ForeignKey(User, related_name='links', default=_user)
    title = models.CharField(_(u'title'), max_length=128)
    timestamp = models.DateTimeField(_(u'post date and time'), auto_now_add=True)
    url = models.URLField(_(u'url address'))
    CATEGORY_CHOICES = (
        (u'CO', u'Cosmos'),
        (u'TC', u'Technology'),
        (u'LH', u'Life Hacks'),
        (u'PO', u'Politics'),
        (u'BG', u'Blogs'),
    )    
    category = models.CharField(_(u'category'), max_length=2, choices=CATEGORY_CHOICES)
    description = models.TextField(_('description'), blank=True)

    def get_absolute_url(self):
        return '%s' % self.url

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('category', '-timestamp', 'title')


####
## ADMIN

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class EntryAdmin(admin.ModelAdmin):
    def get_author(self, obj):
        return '%s' % obj.author
    get_author.short_description = u'Author'

    list_display = ('title', 'timestamp', 'get_author')
    fieldsets = (
        (None, {'fields': ('author',)}),
        ('Entry information', {'fields': ('title', 'timestamp')}),
        #('Entry information', {'fields': ('title',)}),
        ('Entry content', {'fields': ('html', 'body',)}),
    )
    inlines = (ImageInline,)


## Link
class LinkAdmin(admin.ModelAdmin):
    def get_author(self, obj):
        return '%s' % obj.author
    get_author.short_description = u'Author'

    list_display = ('title', 'category', 'timestamp', 'get_author')


####
## REGISTER
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)
