# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
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

from django.contrib.auth.models import User


# ABOUT ME

class MyUser(User):
    alternative_email = models.EmailField()


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
    description = models.TextField()
    
    def __unicode__(self):
        return self.first_name + ' ' + self.middle_name[0] + '. ' +  self.last_name


# Source
class Source(models.Model):
    person = models.ForeignKey(Person, null=True)
    priority = models.IntegerField()
    title = models.CharField(max_length=127)
    url = models.URLField()

    def __unicode__(self):
        return self.title


# Document
class Document(models.Model):
    person = models.ForeignKey(Person, null=True)
    title = models.CharField(max_length=32)
    description = models.TextField()
    document = models.FileField(blank=True, null=True, upload_to="aboutme/doc/")
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title


## ADMIN

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'person')

class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'priority', 'person')


## ADMIN REGISTER
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Source, SourceAdmin)
