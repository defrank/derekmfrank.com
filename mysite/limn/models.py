# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - limn
#
# DESCRIPTION
#   Models definition for User Profile.
#

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


import os, urlparse


####
## MODELS

## User profile:
class UserProfile(models.Model):
    """
    An extension to the User model class to hold more information 
    about a user.

    User is required. Other fields are optional.
    """
    user = models.OneToOneField(User)
    middle_name = models.CharField(_(u'middle name'), max_length=32, blank=True)
    title = models.CharField(_(u'user title or occupation'), max_length=64, blank=True)
    alternative_email = models.EmailField(_(u'alternative email address'), blank=True)
    def get_upload_dir(instance, filename):
        upload_file = 'limn/%s/image/%s' % (instance.user.username, filename)
        return upload_file
    image = models.ImageField(_(u'user image'), upload_to=get_upload_dir, blank=True)
    description = models.TextField(_(u'user description'), blank=True)
    html_description = models.TextField(_(u'html user description'), blank=True)

    def __unicode__(self):
        if self.middle_name:
            return self.first_name + ' ' + self.middle_name[0] + '. ' + self.last_name
        return self.first_name + ' ' + self.last_name


## User images:
class UserImage(models.Model):
    """
    An image for a User.

    """
    user = models.ForeignKey(User)
    title = models.CharField(_('image title'), max_length=64, unique=True, blank=True)
    def get_upload_dir(instance, filename):
        return 'limn/%s/img/%s' % (instance.user.username, filename)
    image = models.ImageField(_('upload user image'), upload_to=get_upload_dir)

    def Meta(self):
        ordering = ['user', 'title']

    def __unicode__(self):
        if self.title:
            return self.title
        return self.image.url


## User documents:
class UserDocument(models.Model):
    """
    A document for a User that may be uploaded or linked via url.

    User and title are required. Other fields are optional.
    """
    user = models.ForeignKey(User)
    title = models.CharField(_(u'document title'), max_length=32)
    def get_upload_dir(instance, filename):
        return 'limn/%s/doc/%s' % (instance.user.username, filename)
    file = models.FileField(_(u'document file'), upload_to=get_upload_dir, blank=True)
    url = models.URLField(_(u'document link'), blank=True)
    description = models.TextField(_(u'document description'), blank=True)

    def Meta(self):
        ordering = ['user', 'title']

    def __unicode__(self):
        if self.file:
            return self.title + ' (' + os.path.splitext(os.path.basename(self.file.path))[-1] + ' format)'
        elif self.url:
            return self.title + ' (hosted on: ' + urlparse.urlsplit(self.url).netloc + ')'
        return self.title


## User sources:
class UserSource(models.Model):
    """
    A source/link for a User.

    User and url are required. Other fields are optional.
    """
    user = models.ForeignKey(User)
    url = models.URLField(_(u'source link'))
    description = models.TextField(_(u'source description'), blank=True)
    priority = models.IntegerField(_(u'source priority'), blank=True)

    def Meta(self):
        ordering = ['user', 'priority', 'url']
        
    def __unicode__(self):
        return urlparse.urlsplit(self.url).netloc


class UserHobbySource(UserSource):
    """
    A hobby source/link for a User.

    Extended from UserSource.
    """


class UserProfileSource(UserSource):
    """
    A profile source/link for a User.

    Extended from UserSource.
    """
    def __unicode__(self):
        return urlparse.urlsplit(self.url).netloc + ' Profile'


class UserRepositorySource(UserSource):
    """
    A repository source/link for a User.

    Extended from UserSource.
    """
    def __unicode__(self):
        return urlparse.urlsplit(self.url).netloc + ' Repository'


####
## ADMIN

## User Profile
class UserImageInline(admin.TabularInline):
    model = UserImage
    extra = 1
                      
class UserDocumentInline(admin.TabularInline):
    model = UserDocument
    extra = 1

class UserSourceInline(admin.TabularInline):
    model = UserSource
    extra = 1

class UserProfileSourceInline(UserSourceInline):
    model = UserProfileSource

class UserRepositorySourceInline(UserSourceInline):
    model = UserRepositorySource

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_username', 'get_email', 'title')
    inlines = [
        UserImageInline, 
        UserDocumentInline, 
        UserRepositorySourceInline, 
        UserProfileSourceInline, 
        UserSourceInline
    ]

    def get_username(self, obj):
        return '%s' % obj.user.username
    get_username.short_description = u'Username'

    def get_first_name(self, obj):
        return '%s' % obj.user.first_name
    get_first_name.short_description = u'First name'

    def get_last_name(self, obj):
        return '%s' % obj.user.last_name
    get_last_name.short_description = u'Last name'

    def get_email(self, obj):
        return '%s' % obj.user.email
    get_email.short_description = u'Email'


####
## REGISTER
admin.site.register(UserProfile, UserProfileAdmin)
