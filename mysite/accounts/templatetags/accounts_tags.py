# $Id: accounts_tags.py,v 1.1 2013-06-30 17:02:40-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   accounts_tags.py - utils
#
# DESCRIPTION
#   Custom template tags and filters.
#

from django import template
register = template.Library()

####
## TAGS

@register.tag
def nameof(parser, token):
    try:
        tag_name, user_var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%r tag requires a single argument' % token.split_contents()[0])
    return NameOfNode(user_var)


class NameOfNode(template.Node):
    def __init__(self, user_var):
        self.user = template.Variable(user_var)

    def render(self, context):
        try:
            myuser = self.user.resolve(context)
            try:
                 return u'%s' % (myuser.get_profile() or myuser.get_full_name() or myuser.get_short_name() or myuser)
            except AttributeError:
                return u'%s' % (myuser.get_full_name() or myuser.get_short_name() or myuser)
        except template.VariableDoesNotExist:
            return ''
