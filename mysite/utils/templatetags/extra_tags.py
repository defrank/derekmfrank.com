# $Id: functions.py,v 1.1 2013-05-28 22:00:02-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   extra_tags.py - utils
#
# DESCRIPTION
#   Custom template tags and filters.
#

from django import template
register = template.Library()

####
## TAGS

# djangosnippets.org/snippets/2196/
@register.tag
def collect(parser, token):
    bits = list(token.split_contents())
    if len(bits) > 3 and bits[-2] == 'as':
        varname = bits[-1]
        items = bits[1:-2]
        return CollectNode(items, varname)
    else:
        raise template.TemplateSyntaxError('%r expected format is "item [item ...] as varname"' % bits[0])


class CollectNode(template.Node):
    def __init__(self, items, varname):
        self.items = map(template.Variable, items)
        self.varname = varname

    def render(self, context):
        context[self.varname] = [ i.resolve(context) for i in self.items ]
        return ''
