# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - aboutme
#
# DESCRIPTION
#   Models definition for mysite about me.
#

from django.db import models
from django.contrib import admin
from mysite.models import SOURCE_TYPE, DOC_TYPE


# ABOUT ME

# Document
class Document(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    type = models.CharField(max_length=4, null=True, choices=DOC_TYPE)
    document = models.FileField(blank=True, null=True, upload_to="aboutme/doc/")
    url = models.URLField(blank=True, null=True, verify_exists=True)

    def __unicode__(self):
        if self.type:
            return self.title + ' (' + self.type + ')'
        return self.title


# Source
class Source(models.Model):
    priority = models.IntegerField()
    title = models.CharField(max_length=127)
    type = models.CharField(max_length=4, choices=SOURCE_TYPE, blank=True, null=True)
    url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.title


# Person
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    title = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="aboutme/img/")
    email = models.EmailField()
    email_name = models.CharField(null=True, max_length=32)
    alternative_email = models.EmailField()
    alternative_email_name = models.CharField(null=True, max_length=32)
    documents = models.ManyToManyField(Document)
    sources = models.ManyToManyField(Source, blank=True, null=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.first_name + ' ' + self.middle_name[0] + '. ' +  self.last_name


## ADMIN

class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class SourceAdmin(admin.ModelAdmin):
    list_display = ('priority', 'title', 'type', 'url')


## ADMIN REGISTER
admin.site.register(Person, PersonAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Source, SourceAdmin)
