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


## ABOUT ME

REPO_CHOICES = (
    (u'GH', u'GitHub'),
    (u'BB', u'BitBucket'),
    (u'RP', u'Repo'),
)


# Document
class Document(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    document = models.FileField(upload_to="doc/aboutme/")

    def __unicode__(self):
        return self.title


# Link
class Link(models.Model):
    title = models.CharField(max_length=64)
    url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.title

 
# Person
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    image = models.ImageField(blank=True, null=True, upload_to="img/aboutme/")
    email = models.EmailField()
    alternative_email = models.EmailField()
    documents = models.ManyToManyField(Document)
    sources = models.ManyToManyField(Link)
    description = models.TextField()
    
    def __unicode__(self):
        return self.first_name + ' ' + self.middle_name + ' ' +  self.last_name


## ADMIN

class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


## ADMIN REGISTER
admin.site.register(Person, PersonAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Link, LinkAdmin)
