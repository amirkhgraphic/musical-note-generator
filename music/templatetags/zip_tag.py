from django import template

register = template.Library()

@register.filter
def zipper(a, b):
    return zip(a, b)
