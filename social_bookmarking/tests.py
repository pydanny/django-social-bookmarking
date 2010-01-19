from django.conf import settings
from django.contrib.auth.models import User
from django.template import Context, Template
from django.template.loader import get_template_from_string
from django.test import TestCase


class TestBookmarks(TestCase):
    fixtures = ['bookmarks.json',]
    
    def setUp(self):
        
        self.user = User(username="bookmark_user")
        self.user.save()
        
        self.google_test = """<a href="http://www.google.com/bookmarks/mark?op=edit&amp;bkmk=http%3A//python.org&amp;title=bookmark_user" title="Google" rel="nofollow">"""
        
        self.print_test = """<a href="javascript:window.print();" title="Print" rel="nofollow">"""

    
    def tearDown(self):
        pass
    
    def test_template_tag(self):
        """ Does the template tag work without blowing up? """
        
        template = get_template_from_string("""
            {% load social_bookmarking_tags %}
            
            {% show_bookmarks object.username 'http://python.org' %}
        """)
        
        c = Context({'object':self.user, 'MEDIA_URL':settings.MEDIA_URL})
        html = template.render(c)
        self.assertTrue(self.google_test in html)
        self.assertTrue(self.print_test in html)        