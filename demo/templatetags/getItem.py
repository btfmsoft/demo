from django import template

register = template.Library()
@register.filter()
def getItem(x,y):
    try:
        return x[y]
    except:
        return None