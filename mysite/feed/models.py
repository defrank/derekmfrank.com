# $Id: $
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


####
## MODELS

class Message(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('-timestamp', 'title')


####
## ADMIN

class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


####
## REGISTER
admin.site.register(Message, MessageAdmin)
