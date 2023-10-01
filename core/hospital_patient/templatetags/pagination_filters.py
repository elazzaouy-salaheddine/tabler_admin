from django import template

register = template.Library()

@register.filter
def paginate_links(page_obj, url_parameter):
    links = []
    if page_obj.has_previous():
        links.append(
            (page_obj.previous_page_number(), '&laquo;', 'page-link')
        )
    else:
        links.append((None, '&laquo;', 'page-link disabled'))

    for i in page_obj.paginator.page_range:
        if page_obj.number == i:
            links.append((i, str(i), 'page-link active'))
        else:
            links.append((i, str(i), 'page-link'))

    if page_obj.has_next():
        links.append(
            (page_obj.next_page_number(), '&raquo;', 'page-link')
        )
    else:
        links.append((None, '&raquo;', 'page-link disabled'))

    return {
        'links': links,
        'url_parameter': url_parameter,
    }
