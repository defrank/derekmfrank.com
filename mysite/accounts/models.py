# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - accounts
#
# DESCRIPTION
#   Models definition for User Profile.
#

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from os.path import basename, splitext
from re import sub
from urlparse import urlsplit

from utils import get_default_user as _user


####
## MODELS

class UserProfile(models.Model):
    """
    An extension to the User model class to hold more information 
    about a user.

    User is required. Other fields are optional.
    """
    user = models.OneToOneField(User, related_name='profile')
    def username(self):
        return '%s' % self.user.username
    def first_name(self):
        return '%s' % self.user.first_name
    middle_name = models.CharField(_(u'middle name'), max_length=32, blank=True)
    def last_name(self):
        return '%s' % self.user.last_name
    title = models.CharField(_(u'title or occupation'), max_length=64, blank=True)
    def email(self):
        return '%s' % self.user.email
    def email_name(self):
        name = sub('^.+[@]', '', self.user.email)
        return sub('[.].+$', '', name)
    alternative_email = models.EmailField(_(u'alternative email address'), blank=True)
    def alternative_email_name(self):
        name = sub('^.+[@]', '', self.alternative_email)
        return sub('[.].+$', '', name)
    description = models.TextField(_(u'description (html okay)'), blank=True)
    def image(self):
        return self.user.images.get(user=self, default=True)

    def images(self):
        return self.user.images.all()

    def documents(self):
        return self.user.documents.all()

    def repositories(self):
        return self.user.repositories.all()

    def profiles(self):
        return self.user.profiles.all()

    def hobbies(self):
        return self.user.hobbies.all()

    def get_absolute_url(self):
        return 'accounts/user/%s/' % self.user.username

    def __unicode__(self):
        if self.user.first_name:
            if self.user.last_name:
                if self.middle_name:
                    return u'%s %c. %s' % (self.user.first_name, self.middle_name[0], self.user.last_name)
                return u'%s %s' % (self.user.first_name, self.user.last_name)
            return u'%s' % self.user.first_name
        elif self.user.last_name:
            return u'%s' % self.user.first_name
        return u'%s' % self.user.username

    class Meta:
        ordering = ('user', 'id')


class Image(models.Model):
    """
    An image for a User.

    User and image are required. Other fields optional.
    """
    user = models.ForeignKey(User, related_name='images', default=_user)
    title = models.CharField(_(u'title'), max_length=64, blank=True)
    def get_upload_dir(instance, filename):
        if instance.title:
            name = '%s%s' % (instance.title, splitext(filename)[-1])
            return 'accounts/%s/img/%s' % (instance.user.username, name)
        return 'accounts/%s/img/%s' % (instance.user.username, filename)
    image = models.ImageField(_(u'upload image'), upload_to=get_upload_dir)
    default = models.BooleanField(_(u'default user image'), default=False)

    def filename(self):
        name = basename(self.image.path)
        if self.title:
            return '%s%s' % (self.title, splitext(name)[-1])
        return name

    def get_absolute_url(self):
        return '%s' % self.image.url

    def __unicode__(self):
        name = basename(self.image.path)
        if self.title:
            return u'%s%s' % (self.title, splitext(name)[-1])
        return u'%s' % name

    """
    @classmethod
    def create(cls, user, title, image, default):
        if default:
            old = Image.objects.get(user=user, default=True)
            old = models.F(False)
            old.save()
        userimage = cls(user=user, title=title, image=image, default=default)
        return userimage
    """
        
    """
    def save(self, *args, **kwargs):
        if self.default:
            old = Image.objects.get(user=self.user, default=True)
            old.default = models.F(False)
            old .save()
        super(Image, self).save(*args, **kwargs)
    """

    class Meta:
        unique_together = ('user', 'default')
        ordering = ('user', 'default', 'title')


class Document(models.Model):
    """
    A document for a User that may be uploaded or linked via url.

    User and title are required. Other fields are optional.
    """
    user = models.ForeignKey(User, related_name='documents', default=_user)
    title = models.CharField(_(u'title'), max_length=32, blank=True)
    def get_upload_dir(instance, filename):
        if instance.title:
            name = '%s%s' % (instance.title, splitext(filename)[-1])
            return 'accounts/%s/doc/%s' % (instance.user.username, name)
        return 'accounts/%s/doc/%s' % (instance.user.username, filename)
    file = models.FileField(_(u'file'), upload_to=get_upload_dir, blank=True, null=True)
    url = models.URLField(_(u'link'), blank=True)
    description = models.TextField(_(u'description'), blank=True)

    def domain(self):
        if self.url:
            return urlsplit(self.url).netloc
        return ''
        
    def filename(self):
        if self.file:
            name = basename(self.file.path)
            if self.title:
                return '%s%s' % (self.title, splitext(name)[-1])
            return '%s' % name
        elif self.url:
            name = self.domain
            if self.title:
                return '%s (hosted on %s)' % (self.title, name)
            return 'unknown (hosted on %s)' % name
        elif self.title:
            return '%s' % self.title
        return ''

    def get_absolute_url(self):
        if self.file:
            return '%s' % self.file.url
        elif self.url:
            return '%s' % self.url
        return ''

    def __unicode__(self):
        if self.file:
            name = basename(self.file.path)
            if self.title:
                return u'%s%s' % (self.title, splitext(name)[-1])
            return u'%s' % name
        elif self.url:
            name = urlsplit(self.url).netloc
            if self.title:
                return u'%s (hosted on %s)' % (self.title, name)
            return u'unknown (hosted on %s)' % name
        elif self.title:
            return u'%s' % self.title
        return u'document %d for %s' % (self.id, self.user)

    class Meta:
        ordering = ('user', 'title')


class Link(models.Model):
    """
    A source/link for a User.

    User and url are required. Other fields are optional.
    """
    url = models.URLField(_(u'link'))
    description = models.TextField(_(u'description'), blank=True)
    priority = models.IntegerField(_(u'priority'), blank=True, null=True)

    def domain(self):
        return '%s' % urlsplit(self.url).netloc

    def get_absolute_url(self):
        return '%s' % self.url
       
    def __unicode__(self):
        return u'%s' % urlsplit(self.url).netloc

    class Meta:
        abstract = True
        ordering = ('priority', 'url')
 

class HobbyLink(Link):
    """
    A hobby source/link for a User.

    Extended from Link.
    """
    user = models.ForeignKey(User, related_name='hobbies', default=_user)

    class Meta:
        ordering = ('user', 'priority', 'url')


class ProfileLink(Link):
    """
    A profile source/link for a User.

    Extended from UserLink.
    """
    user = models.ForeignKey(User, related_name='profiles', default=_user)

    def __unicode__(self):
        return u'%s profile' % urlsplit(self.url).netloc

    class Meta:
        ordering = ('user', 'priority', 'url')


class RepositoryLink(Link):
    """
    A repository source/link for a User.

    Extended from Link.
    """
    user = models.ForeignKey(User, related_name='repositories', default=_user)

    def __unicode__(self):
        return u'%s repository' % urlsplit(self.url).netloc

    class Meta:
        ordering = ('user', 'priority', 'url')


####
## INLINES

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
                      
class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0

class LinkInline(admin.TabularInline):
    model = Link
    extra = 0

class HobbyLinkInline(LinkInline):
    model = HobbyLink

class ProfileLinkInline(LinkInline):
    model = ProfileLink

class RepositoryLinkInline(LinkInline):
    model = RepositoryLink

   
####
## ADMIN

class ProfileAdmin(admin.ModelAdmin):
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
        ImageInline, 
        DocumentInline, 
        RepositoryLinkInline, 
        ProfileLinkInline, 
        LinkInline
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = ('filename', 'user', 'default')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'user', 'description')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('domain', 'user', 'priority', 'description')
    fieldsets = (
        (None, {'fields': ('user', 'url', 'description', 'priority')}),
    )


####
## REGISTER
#admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register((RepositoryLink, ProfileLink, HobbyLink), LinkAdmin)
