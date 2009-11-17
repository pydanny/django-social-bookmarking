import urlparse

from django.template import Library
from django.utils.http import urlquote

from social_bookmarking.models import Bookmark

register = Library()

class NoRequestContextProcessorFound(Exception):
    pass

@register.inclusion_tag('social_bookmarking/links.html', takes_context=True)
def show_bookmarks(context, title, object_or_url, description=""):
    """ Displays the bookmarks
        TODO: Add in the javascript cleanup part
    """

    if hasattr(object_or_url, 'get_absolute_url'):
        url = getattr(object_or_url, 'get_absolute_url')()

    url = unicode(object_or_url)
    
    if not url.startswith('http'):
        url = context['request'].build_absolute_uri(url)

    # TODO: Bookmark should have a .active manager:
    bookmarks = Bookmark.objects.filter(status=2).values()

    for bookmark in bookmarks:
        bookmark['description'] = description
        bookmark['link'] = bookmark['url'] % {'title': urlquote(title),
                                        'url': urlquote(url),
                                        'description': urlquote(description)
                                       }


    return {'bookmarks':bookmarks, 'MEDIA_URL': context['MEDIA_URL']}

