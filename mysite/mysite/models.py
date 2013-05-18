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

## BLOG
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


## PORTFOLIO
class Portfolio(models.Model):
    title = models.CharField(max_length=150)

class PortfolioEntry(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
