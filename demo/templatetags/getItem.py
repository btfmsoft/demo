from django import template

register = template.Library()
@register.filter()
def getItem(x,y):
    return x[y]