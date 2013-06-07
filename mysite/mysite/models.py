# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - mysite
#
# DESCRIPTION
#   A models (database bridge) definition for mysite derekmfrank.com.
#

from django.db import models
from django.contrib import admin


## HOME CONTENT

class Message(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.title

class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


## REGISTER
admin.site.register(Message, MessageAdmin)
