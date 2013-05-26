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

# Project
class Project(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.title


DEPARTMENT_CHOICES = (
    (u'CS', u'Computer Science'),
    (u'CE', u'Computer Engineering'),
    (u'CGD', u'Computer Game Design'),
    (u'EE', u'Electrical Engineering'),
    (u'RE', u'Robotics Engineering'),
    (u'TIM', u'Technology and Information Management'),
    (u'AMS', u'Applied Mathematics and Statistics'),
    (u'MA', u'Mathematics'),
    (u'AM', u'Applied Mathematics'),
    (u'ST', u'Statistics'),
    (u'PH', u'Physics'),
    (u'MC', u'Miscellaneous'),
)

# Education
class Education(models.Model):
    school_name = models.CharField(null=True, max_length=127)
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
    coursework_repository = models.URLField(blank=True, null=True, verify_exists=True)

    def __unicode__(self):
        return self.school_name


# Course
class Course(models.Model):
    education_institution = models.ForeignKey(Education)
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, default=u'MC')
    course_name = models.CharField(max_length=127)
    course_number = models.IntegerField()
    course_id = models.CharField(max_length=16)
    course_url = models.URLField(blank=True, null=True, verify_exists=True)
    course_repository = models.URLField(blank=True, null=True, verify_exists=True)
    course_repository_name = models.CharField(blank=True, null=True, max_length=32)
    description = models.TextField()

    def __unicode__(self):
        return self.course_name


# Assignment
class Assignment(models.Model):
    course = models.ForeignKey(Course)
    assignment_name = models.CharField(max_length=127)
    assignment_number = models.IntegerField()
    assignment_id = models.CharField(max_length=16)
    assignment_url = models.URLField(blank=True, null=True, verify_exists=True)
    assignment_repository = models.URLField(blank=True, null=True, verify_exists=True)
    assignment_repository_name = models.CharField(blank=True, null=True, max_length=32)
    description = models.TextField()

    def __unicode__(self):
        return self.assignment_name


## PORTFOLIO ADMIN

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'graduation_date')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_id', 'department', 'education_institution')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('assignment_name', 'assignment_id', 'course')

## REGISTER
admin.site.register(Education, EducationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)
