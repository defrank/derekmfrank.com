# $Id: $
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


## PORTFOLIO

REPO_CHOICES = (
    ('GH', 'GitHub'),
    ('BB', 'BitBucket'),
    ('RE', 'Repo'),
)

LANGUAGE_CHOICES = (
    ('c', 'C'),
    ('cpp', 'C++'),
    ('java', 'Java'),
    ('clisp', 'Common Lisp'),
    ('lua', 'Lua'),
    ('m', 'Matlab'),
    ('oc', 'OCaml'),
    ('oct', 'Octave'),
    ('pl', 'Perl'),
    ('prolog', 'Prolog'),
    ('py', 'Python'),
    ('scm', 'Scheme'),
    ('st', 'Smalltalk'),
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


# Project
class Project(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.title


# Education
class Education(models.Model):
    school_name = models.CharField(null=True, max_length=127)
    acronym = models.CharField(blank=True, null=True, max_length=8)
    DEGREE_CHOICES = (
        (u'BS', u'Bachelor of Science'),
        (u'BA', u'Bachelor of Arts'),
        (u'MS', u'Master of Science'),
        (u'MA', u'Master of Arts'),
    )
    degree = models.CharField(max_length=3, choices=DEGREE_CHOICES)
    major = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    minor = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    graduation_date = models.DateField()
    coursework_repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    coursework_repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES) 

    def __unicode__(self):
        return self.acronym or self.school_name


# Course
class Course(models.Model):
    education_institution = models.ForeignKey(Education)
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, default=u'MC')
    course_name = models.CharField(max_length=127)
    course_number = models.CharField(max_length=8, null=True)
    course_lab_letter = models.CharField(max_length=4, blank=True, null=True)
    course_url = models.URLField(blank=True, null=True, verify_exists=True)
    course_lab_url = models.URLField(blank=True, null=True, verify_exists=True)
    course_repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    course_repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES)
    description = models.TextField()

    def __unicode__(self):
        if self.course_lab_letter:
            return  self.course_name + ' (' + self.department + ' ' + self.course_number + '/' + self.course_lab_letter + ')' 
        return  self.course_name + ' (' + self.department + ' ' + self.course_number + ')' 
        #return self.course_name + ' (' + self.department + ')'


# Assignment
class Assignment(models.Model):
    course = models.ForeignKey(Course)
    assignment_name = models.CharField(max_length=127)
    assignment_number = models.IntegerField()
    assignment_id = models.CharField(max_length=16)
    programming_language = models.CharField(max_length=8, blank=True, null=True, choices=LANGUAGE_CHOICES)
    assignment_url = models.URLField(blank=True, null=True, verify_exists=True)
    assignment_repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    assignment_repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.course.course_id + ' - ' + self.assignment_id + ' - ' +  self.assignment_name


## PORTFOLIO ADMIN

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'acronym', 'degree', 'major', 'graduation_date')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'department', 'course_number', 'course_lab_letter', 'education_institution')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('assignment_name', 'assignment_id', 'programming_language', 'course')

## REGISTER
admin.site.register(Education, EducationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)
