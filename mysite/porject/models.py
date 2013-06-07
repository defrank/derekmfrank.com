# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - portfolio
#
# DESCRIPTION
#   A  portfolio models definition for mysite derekmfrank.com.
#

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User as Owner
from django.utils.translation import ugettext_lazy as _

import urlparse


####
## HELPERS




####
## MODELS

## Project:
class Project(models.Model):
    """
    Holds a portfolio project.

    Owner, title, description, and date are required. Other fields are 
    optional.
    """
    owner = models.ForeignKey(Owner)
    title = models.CharField(_(u'project title'), max_length=128)
    description = models.TextField(_(u'project description'), blank=True)
    date = models.DateField(_(u'project date'))
    url = models.URLField(_(u'project website link'), blank=True)
    repository_url = models.URLField(_(u'project repository link'), blank=True)

    def get_repository_name(self):
        if repository_url:
            return urlparse.urlsplit(self.repository_url).netloc
        return None

    def Meta(self):
        ordering = ['owner', '-date', 'title']

    def __unicode__(self):
        return self.title


class ProjectProgrammingLanguage(models.Model):
    """
    A project programming language.

    Project is required. Other fields are optional.
    """
    project = models.ForeignKey(Project)
    language = models.CharField(_(u'project programming language'), max_length=16, blank=True)
    version = models.CharField(_(u'programming language version'), max_length=16, blank=True)
    framework = models.CharField(_(u'programming language framework'), max_length=16, blank=True)
    framework_version = models.CharField(_(u'programming language framework version'), max_length=16, blank=True)
    description = models.TextField(_(u'project programming language description'), blank=True)

    def Meta(self):
        ordering = ['project', 'language', 'version', 'framework', 'framework_version']

    def __unicode__(self):
        if self.language and self.framework:
            return self.language + self.version + '/' + self.framework + self.framework_version
        elif self.language:
            return self.language + self.version
        elif self.framework:
            return self.framework + self.framework_version
        return self.project


DEPARTMENT_CHOICES = (
    (u'CS', u'Computer Science'),
    (u'CE', u'Computer Engineering'),
    (u'CGD', u'Computer Game Design'),
    (u'EE', u'Electrical Engineering'),
    (u'RE', u'Robotics Engineering'),
    (u'BE', u'Biomolecular Engineering'),
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
class Education(models.Model):
    """
    An education institution where a degree was earned.

    Owner, name, degree, and graduation date aer required. Other fields
    optional.
    """
    owner = models.ForeignKey(Owner)
    name = models.CharField(_(u'institution name'), max_length=128)
    acronym = models.CharField(_(u'institution acronym'), max_length=8, blank=True)
    DEGREE_CHOICES = (
        (u'BS', u'Bachelor of Science'),
        (u'BA', u'Bachelor of Arts'),
        (u'MS', u'Master of Science'),
        (u'MA', u'Master of Arts'),
        (u'HSD', u'High School Diploma'),
        (u'GED', u'G.E.D.'),
    )
    degree = models.CharField(_(u'institution degree awarded'), max_length=3, choices=DEGREE_CHOICES)
    major = models.CharField(_(u'degree major study'), max_length=4, choices=DEPARTMENT_CHOICES, blank=True)
    minor = models.CharField(_(u'degree minor study'), max_length=4, choices=DEPARTMENT_CHOICES, blank=True)
    graduation_date = models.DateField(_(u'graduation date'))
    repository_url = models.URLField(_(u'coursework repository link'), blank=True)

    def get_repository_name(self):
        if repository_url:
            return urlparse.urlsplit(self.repository_url).netloc
        return None

    def Meta(self):
        ordering = ['owner', '-graduation_date', 'name', 'acronym']
        verbose_name_plural = 'education'

    def __unicode__(self):
        return self.acronym or self.name


class Course(models.Model):
    """
    A course taken at an education institution.

    Education, department, title, and course number are
    required. Other fields optional.
    """
    education = models.ForeignKey(Education)
    department = models.CharField(_(u'course department'), max_length=4, choices=DEPARTMENT_CHOICES)
    title = models.CharField(_(u'course name'), max_length=128)
    number = models.CharField(_(u'course number'), max_length=8)
    lab = models.CharField(_(u'course laboratory letter'), max_length=4, blank=True)
    url = models.URLField(_(u'course website link'), blank=True)
    lab_url = models.URLField(_(u'course laboratory website link'), blank=True)
    repository_url = models.URLField(_(u'course repository link'), blank=True)
    description = models.TextField(_(u'course description'), blank=True)

    def get_repository_name(self):
        if repository_url:
            return urlparse.urlsplit(self.repository_url).netloc
        return None

    def __unicode__(self):
        if self.lab:
            return  self.name + ' (' + self.department + ' ' + self.number + '/' + self.lab + ')' 
        return  self.name + ' (' + self.department + ' ' + self.number + ')' 


class Assignment(models.Model):
    """
    An assignment for a Course.

    Course, title, and identification are required. Other fields
    optional.
    """
    course = models.ForeignKey(Course)
    title = models.CharField(_(u'assignment title'), max_length=128)
    identification = models.CharField(_(u'assignment identification'), max_length=16)
    programming_language = models.OneToOneField(ProjectProgrammingLanguage, blank=True)
    url = models.URLField(_(u'assignment website link'), blank=True)
    repository_url = models.URLField(_(u'assignment repository link'), blank=True)
    description = models.TextField(_(u'assignment description'), blank=True)

    def get_repository_name(self):
        if repository_url:
            return urlparse.urlsplit(self.repository_url).netloc
        return None

    def Meta(self):
        ordering = ['course', 'identification', 'title']

    def __unicode__(self):
        if self.course.lab:
            return self.course.department + self.course.number + '/' + self.course.lab + ' - ' + self.identification + ' - ' +  self.title
        return self.course.department + self.course.number + ' - ' + self.identification + ' - ' +  self.title


class AssignmentProgrammingLanguage(ProjectProgrammingLanguage):
    """
    An assignmen programming language.
    Extends ProjectProgrammingLanguage.

    Project is required. Other fields are optional.
    """
    project = models.ForeignKey(Assignment)

    def Meta(self):
        ordering = ['project', 'language', 'version', 'framework', 'framework_version']

    def __unicode__(self):
        if self.language and self.framework:
            return self.language + self.version + '/' + self.framework + self.framework_version
        elif self.language:
            return self.language + self.version
        elif self.framework:
            return self.framework + self.framework_version
        return self.project




####
## ADMIN

# Project
class ProjectProgrammingLanguageInline(admin.TabularInline):
    model = ProjectProgrammingLanguage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return '%s' % obj.owner.get_profile()
    get_owner.short_description = u'Project Owner'
    list_display = ('title', 'get_repository_name', 'date', 'get_owner', 'description')
    inlines = [ProjectProgrammingLanguageInline]


## Education
class CourseInline(admin.TabularInline):
    models = Course
    extra = 3

class AssignmentInline(admin.TabularInline):
    models = Assignment
    extra = 2

class AssignmentProgrammingLanguageInline(admin.TabularInline):
    models = AssignmentProgrammingLanguage
    extra = 1

class EducationAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return '%s' % obj.owner
    get_owner.short_description = u'Project Owner'
    list_display = ('get_owner', 'name', 'acronym', 'degree', 'major', 'graduation_date')
    inlines = [
        CourseInline,
        AssignmentInline,
        AssignmentProgrammingLanguageInline,
    ]


class CourseAdmin(admin.ModelAdmin):
    def get_education(self, obj):
        return '%s' % obj.education
    get_education.short_description = u'Education institution'
    list_display = ('title', 'department', 'number', 'lab', 'get_education')



class AssignmentAdmin(admin.ModelAdmin):
    def get_course(self, obj):
        return '%s' % obj.course
    get_course.short_description = u'Course'
    list_display = ('title', 'identification', 'programming_language', 'get_course')



####
## REGISTER
admin.site.register(Project, ProjectAdmin)
admin.site.register(Education, EducationAdmin)
