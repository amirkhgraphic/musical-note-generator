from django import template

register = template.Library()

@register.filter
def zipper(a, b):
    return zip(a, b)

@register.filter
def percent_view(a):
    return f'{int(float(a) * 100)}%'
