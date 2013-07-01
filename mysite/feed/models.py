# $Id: models.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - feed
#
# DESCRIPTION
#   A models definition for mysite news feed.
#

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from utils import get_default_user as _user, markdown_to_html


####
## MODELS

class News(models.Model):
    """
    News or message update.

    Title, body, and timestamp are required.
    """
    author = models.ForeignKey(User, default=_user)
    title = models.CharField(_(u'title'), max_length=150)
    html = models.BooleanField(_('html in body?'))
    body = models.TextField(_(u'body text'))
    timestamp = models.DateTimeField(_(u'last updated'), auto_now=True, auto_now_add=True)

    def body_html(self):
        if self.html:
            images = self.images.all()
            return markdown_to_html(self.body, images)
        return self.body

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('-timestamp', 'title')
        verbose_name = 'news'
        verbose_name_plural = 'news'


class Image(models.Model):
    """
    Image for News post.

    """
    news = models.ForeignKey(News, related_name='images')
    title = models.CharField(_(u'title'), max_length=128)
    def get_upload_dir(instance, filename):
        return 'feed/%s/news%d/%s' % (instance.author.username, instance.news.id, filename)
    image = models.ImageField(_(u'upload image'), upload_to=get_upload_dir, blank=True, null=True)
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
        if self.title:
            return u'%s' % self.title
        elif self.image:
            return u'%s' % self.image.get_filename
        elif self.url:
            return u'%s' % self.url
        return u'image %d for news feed post %d: %s' % (self.id, self.news.id, self.news)

    class Meta:
        ordering = ('-news', 'title')


####
## ADMIN

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    inlines = (ImageInline,)


####
## REGISTER
admin.site.register(News, NewsAdmin)
