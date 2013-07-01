# $Id: models.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
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
    user = models.OneToOneField(User, related_name='contact_info')
    body = models.TextField(_('contact information'))

    def __unicode__(self):
        return u'%s' % self.body

    class Meta:
        ordering = ('user', 'body')
        verbose_name = u'contact information'
        verbose_name_plural = u'contact information'


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
    def get_user(self, obj):
        return '%s' % obj.user.get_full_name()
    get_user.short_description = u'Full name'
    list_display = ('get_user', 'body')

class TopicAdmin(admin.ModelAdmin):
    def get_user(self, obj):
        return '%s' % obj.user.get_full_name()
    get_user.short_description = u'Full name'
    list_display = ('get_user', 'title')
    inlines = (BulletInline,)


####
## REGISTER
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(Topic, TopicAdmin)
