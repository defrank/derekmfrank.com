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


## CHOICES

SOURCE_TYPE = (
    ('RP', 'Repository'),
    ('PF', 'Profile'),
    ('EX', 'Extra'),
)

PROFILE_CHOICES = (
    ('SE', 'StackExchange'),
    ('LI', 'LinkedIn'),
    ('FM', 'Flavors.me'),
    ('BY', 'Beyond'),
    ('FB', 'Facebook'),
    ('PR', 'Profile'),
)

REPO_CHOICES = (
    (u'GH', u'GitHub'),
    (u'BB', u'BitBucket'),
    (u'RP', u'Repo'),
)

LANGUAGE_TYPES = (
    ('scr', 'Scripting'),
    ('prgm', 'Programming'),
    ('mkup', 'Markup'),
)

LANGUAGE_CHOICES = (
    ('c', 'C'),
    ('cpp', 'C++'),
    ('css', 'CSS'),
    ('java', 'Java'),
    ('js', 'Javascript'),
    ('clisp', 'Common Lisp'),
    ('html', 'HTML'),
    ('htmlcss', 'HTML/CSS'),
    ('lua', 'Lua'),
    ('m', 'Matlab'),
    ('oc', 'OCaml'),
    ('oct', 'Octave'),
    ('pl', 'Perl'),
    ('prolog', 'Prolog'),
    ('py', 'Python'),
    ('pydj', 'Python/Django'),
    ('scm', 'Scheme'),
    ('st', 'Smalltalk'),
)

FRAMEWORK_CHOICES = (
    ('dj', 'Django'),
)

DB_CHOICES = (
    ('sql', 'MySQL'),
    ('pgs', 'PostgreSQL'),
    ('pgsp', 'PostgreSQL Psycopg2'),
    ('lite', 'SQLite'),
    ('orac', 'Oracle'),
)

DEPARTMENT_CHOICES = (
    (u'CS', u'Computer Science'),
    (u'CE', u'Computer Engineering'),
    (u'CGD', u'Computer Game Design'),
    (u'EE', u'Electrical Engineering'),
    (u'RE', u'Robotics Engineering'),
    (u'TIM', u'Technology and Information Management'),
    (u'AMS', u'Applied Mathematics and Statistics'),
    (u'Math', u'Mathematics'),
    (u'AM', u'Applied Mathematics'),
    (u'Stat', u'Statistics'),
    (u'Phys', u'Physics'),
    (u'Econ', u'Economics'),
    (u'Psyc', u'Psychology'),
    (u'Musc', u'Music'),
    (u'Lit', u'Literature'),
    (u'Writ', u'Writing'),
    (u'Stev', u'Stevenson'),
    (u'MC', u'Miscellaneous'),
)


## HOME CONTENT

class Message(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return self.title

class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


## REGISTER
admin.site.register(Message, MessageAdmin)
