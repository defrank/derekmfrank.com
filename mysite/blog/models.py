# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - blog
#
# DESCRIPTION
#   Models definition for mysite blog.
#

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
