# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - mff
#
# DESCRIPTION
#   Models definition for MFF pages.
#

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


####
## MODELS

class ContactInformation(models.Model):
    user = models.OneToOneField(User, related_name='contact')
    body = models.TextField(_('contact information'))

    def __unicode__(self):
        return u'%s' % self.body

    class Meta:
        ordering = ('user', 'body')


class Topic(models.Model):
    user = models.ForeignKey(User, related_name='topics')
    title = models.CharField(_('title'), max_length=128)
    bullets_body = models.TextField(_('bullet body pre-text'), blank=True)
    body = models.TextField(_('body'), blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('user', 'title')


class Bullet(models.Model):
    topic = models.ForeignKey(Topic, related_name='bullets')
    body = models.TextField(_('body'))

    def __unicode__(self):
        return u'%s' % self.body

    class Meta:
        ordering = ('topic', 'id')


####
## INLINES

class BulletInline(admin.TabularInline):
    model = Bullet
    extra = 0


####
## ADMIN

class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'body')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    inlines = (BulletInline,)


####
## REGISTER
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(Topic, TopicAdmin)
