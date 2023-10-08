# Create a custom Django filter in your app (e.g., myapp/templatetags/custom_filters.py)
from django import template

register = template.Library()


@register.filter
def list_slice(lst, start):
    return lst[start:]
