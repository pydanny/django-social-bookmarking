=========================
Django Social Bookmarking
=========================

A common use case in building applications is to provide links to social networking services. There are 
other Django apps that do this already, but they suffer from having the links stored statically and/or
have licenses we can't use effectively in a US Federal government environment.

This solution provides the following:

 * A MIT license. 
 * Target social bookmarking sites stored in a model
 * Admin tools 
 * A fixture of 14 target sites
 * Icons for each of those target sites and many more
 * A test application to confirm that the basic view works
 * Eggification for easy installation and control
 
Installation
------------

Via pip::

    easy_install django-social-bookmarking
    
Via easy_setup::

    pip install django-social-bookmarking
    
Add *'social_bookmarking'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'social_bookmarking',
        )
        
Synch the database::

    ./manage.py syncdb
    
Load the fixtures::

    ./manage.py loaddata <location-of-django-social-bookmarking>/social_bookmarking/fixtures/bookmarks.json
    
Depending on your setup, you may need to copy the media files to your local media 
folder::

    cp -R <location-of-django-social-bookmarking>/social_bookmarking/media/social_bookmarking <my-project>/media/
    
Usage
-----

At the top of your page::

    {% load social_bookmarking_tags %}
    
    {% show_bookmarks object.title 'full-http-path-to-object' object.description %}
    
**Note**: The ``object.description`` field is optional.

Todo
-----

 * Add more social networking sites
 * Validation existing social networking sites. Sounds like a test to me!
 * Full suite of tests against each site stored in the fixture.


Other Django Social Bookmarking applications
--------------------------------------------

Django Social Bookmarking is a very rough fork of these two applications. 

 * `django-social-bookmarks <http://bitbucket.org/trbs/django-social-bookmarks/>`_
 
 * `django-sociable <http://bitbucket.org/kmike/django-sociable/>`_

