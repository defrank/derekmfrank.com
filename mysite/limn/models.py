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
    description = models.TextField(_(u'user description'), blank=True)
    html_description = models.TextField(_(u'html user description'), blank=True)

    def __unicode__(self):
        if self.middle_name:
            return u'%s %c. %s' % (self.user.first_name, self.middle_name[0], self.user.last_name)
        return u'%s %s' % (self.user.first_name, self.user.last_name)


## User images:
class UserImage(models.Model):
    """
    An image for a User.

    User and image are required. Other fields optional.
    """
    user = models.ForeignKey(UserProfile)
    title = models.CharField(_('image title'), max_length=64, unique=True, blank=True)
    def get_upload_dir(instance, filename):
        return 'limn/%s/img/%s' % (instance.user.user.username, filename)
    image = models.ImageField(_('upload user image'), upload_to=get_upload_dir)
    default = models.BooleanField(_('default user profile image'), default=False)

    def get_absolute_url(self):
        return '%s' % self.image.url

    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        return u'%s' % self.image.url

    class Meta:
        unique_together = ('user', 'default')
        ordering = ('user', 'default', 'title')


## User documents:
class UserDocument(models.Model):
    """
    A document for a User that may be uploaded or linked via url.

    User and title are required. Other fields are optional.
    """
    user = models.ForeignKey(UserProfile)
    title = models.CharField(_(u'document title'), max_length=32)
    def get_upload_dir(instance, filename):
        return 'limn/%s/doc/%s' % (instance.user.user.username, filename)
    file = models.FileField(_(u'document file'), upload_to=get_upload_dir, blank=True, null=True)
    url = models.URLField(_(u'document link'), blank=True)
    description = models.TextField(_(u'document description'), blank=True)

    def get_absolute_url(self):
        if self.file:
            return '%s' % self.file.url
        elif self.url:
            return '%s' % self.url
        return ''

    def __unicode__(self):
        if self.file:
            return u'%s (%s format)' % (self.title, os.path.splitext(os.path.basename(self.file.path))[-1])
        elif self.url:
            return u'%s (hosted on: %s)' % (self.title, urlparse.urlsplit(self.url).netloc)
        return u'%s' % self.title

    class Meta:
        ordering = ('user', 'title')


## User sources:
class UserSource(models.Model):
    """
    A source/link for a User.

    User and url are required. Other fields are optional.
    """
    user = models.ForeignKey(UserProfile)
    url = models.URLField(_(u'source link'))
    description = models.TextField(_(u'source description'), blank=True)
    priority = models.IntegerField(_(u'source priority'), blank=True)

    def get_absolute_url(self):
        return '%s' % self.url
       
    def __unicode__(self):
        return u'%s' % urlparse.urlsplit(self.url).netloc

    class Meta:
        ordering = ('user', 'priority', 'url')
 

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
        return u'%s profile' % urlparse.urlsplit(self.url).netloc


class UserRepositorySource(UserSource):
    """
    A repository source/link for a User.

    Extended from UserSource.
    """
    def __unicode__(self):
        return u'%s repository' % urlparse.urlsplit(self.url).netloc


####
## ADMIN

## User Profile
class UserImageInline(admin.TabularInline):
    model = UserImage
    extra = 0
                      
class UserDocumentInline(admin.TabularInline):
    model = UserDocument
    extra = 0

class UserSourceInline(admin.TabularInline):
    model = UserSource
    extra = 0

class UserProfileSourceInline(UserSourceInline):
    model = UserProfileSource

class UserRepositorySourceInline(UserSourceInline):
    model = UserRepositorySource

class UserProfileAdmin(admin.ModelAdmin):
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

    list_display = ('get_first_name', 'get_last_name', 'get_username', 'get_email', 'title')
    #fieldsets = (
        #(None, {'fields': ('middle_name', 'title', 'alternative_email')}),
        #('Descriptions', {'fields': ('description', 'html_description')}),
    #)
    inlines = (
        UserImageInline, 
        UserDocumentInline, 
        UserRepositorySourceInline, 
        UserProfileSourceInline, 
        UserSourceInline
    )


####
## REGISTER
admin.site.register(UserProfile, UserProfileAdmin)
