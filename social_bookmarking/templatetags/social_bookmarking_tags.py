import os.path
from sys import stderr

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
    
    if isinstance(object_or_url, (str, unicode)):
        url = unicode(object_or_url)
    else:
        url = unicode(getattr(object_or_url, 'get_absolute_url')())        
        
    if not url.startswith('http'):
        # URL does not have leading http so we need to find the http host
            
        http_host = None
        for element in context.dicts:
            if 'request' in element:
                try:
                    http_host = element['request'].META['HTTP_HOST']    
                except AttributeError:
                    msg = """
                            social_bookmarking_tag could not find the META attribute
                            on the http request object."""
                    raise AttributeError(msg)
                except KeyError:
                    msg = """
                            social_bookmarking_tag could not find the HTTP_HOST 
                            key on the META attribute of the http request object."""
                    raise KeyError(msg)
                
                break
    
        if not http_host:
            msg = """
                    No request given to the social_bookmarking_tags template tag. 
                    Please add 'django.core.context_processors.request' to the
                    TEMPLATE_CONTEXT_PROCESSORS in your settings.py file."""
            raise NoRequestContextProcessorFound(msg)
            
        url = 'http://' + http_host + url

    bookmarks = Bookmark.objects.filter(status=2).values()
    
    for bookmark in bookmarks:
        bookmark['description'] = description     
        bookmark['link'] = bookmark['url'] % {'title': urlquote(title),
                                        'url': urlquote(url),
                                        'description': urlquote(description)
                                       }
        
        
    return {'bookmarks':bookmarks, 'MEDIA_URL': context['MEDIA_URL']}
        