from django import template
from django import template

register = template.Library()

@register.inclusion_tag('base/pagination.html', takes_context=True)
def your_custom_pagination(context, page_obj, num_pages_to_display=5):
    # Your pagination logic here
    return {
        'page_obj': page_obj,
        'page_range': page_range,
    }
