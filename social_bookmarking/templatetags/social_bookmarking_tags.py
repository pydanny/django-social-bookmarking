#!python

from string import Template

from django.template import Library
from django.utils.http import urlquote

from social_bookmarking.models import Bookmark

register = Library()

@register.inclusion_tag('social_bookmarking/links.html', takes_context=True)
def show_bookmarks(context, title, object_or_url, description=""):
    
    if isinstance(object_or_url, (str, unicode)):
        url = unicode(object_or_url)
    else:
        url = unicode(getattr(object_or_url, 'get_absolute_url')())
    

    bookmarks = Bookmark.objects.filter(status=2).values()
    
    for bookmark in bookmarks:
        #bkmk = {}
        bookmark['description'] = description     
        bookmark['link'] = bookmark['url'] % {'title': urlquote(bookmark['title']),
                                        'url': urlquote(url),
                                        'description': urlquote(description)
                                       }
        
        #bookmarks.append(bkmk)
        
    return {'bookmarks':bookmarks, 'MEDIA_URL': context['MEDIA_URL']}
        