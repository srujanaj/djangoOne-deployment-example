from django import template

register = template.Library()

@register.filter(name ='cutout')
def cutout(value,arg):
    """
    This cuts out all values of "arg" from a string
    """
    return value.replace(arg,'')

# register.filter('cutout',cutout)
