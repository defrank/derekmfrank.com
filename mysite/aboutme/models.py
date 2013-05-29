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
from mysite.models import SOURCE_TYPE


# ABOUT ME

# Document
class Document(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    document = models.FileField(upload_to="doc/aboutme/")

    def __unicode__(self):
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
    image = models.ImageField(blank=True, null=True, upload_to="img/aboutme/")
    email = models.EmailField()
    alternative_email = models.EmailField()
    documents = models.ManyToManyField(Document)
    sources = models.ManyToManyField(Source, blank=True, null=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.first_name + ' ' +  self.last_name


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
