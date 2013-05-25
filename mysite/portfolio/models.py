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
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.title


# Education
class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    graduation_date = models.DateField()

    def __unicode__(self):
        return self.school


## PORTFOLIO ADMIN

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'graduation_date')

## REGISTER
admin.site.register(Education, EducationAdmin)
