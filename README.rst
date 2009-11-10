=========================
Django Social Bookmarking
=========================

.. contents:: Table of Contents

A common use case in building applications is to provide links to social 
networking services. There are other Django apps that do this already, but they
suffer from having the links stored statically and/or have licenses we can't use
effectively in a US Federal government environment.

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

Install into your Python path. Tag coming soon for easy pip/easy_install.
    
Add *'social_bookmarking'* to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'social_bookmarking',
        )
        
If you have not yet done so, add '*django.core.context_processors.request*'  to 
the TEMPLATE_CONTEXT_PROCESSORS in your settings.py file::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django.core.context_processors.request',
        )
        
Synch the database::

    ./manage.py syncdb
    
Load the fixtures::

    ./manage.py loaddata <location-of-django-social-bookmarking>/social_bookmarking/fixtures/bookmarks.json
    
Depending on your setup, you may need to copy the media files to your local 
media folder::

    cp -R <location-of-django-social-bookmarking>/social_bookmarking/media/social_bookmarking <my-project>/media/
    
----    
    
Usage
-----

At the top of your page::

    {% load social_bookmarking_tags %}
    
    {% show_bookmarks object.title 'full-http-path-to-object' object.description %}
    
    -- or --
    
    {% show_bookmarks object.title object object.description %}    
    
    
**Note**: The ``object.description`` field is optional.

----

Customizations
--------------

Django Social Bookmarking is designed to be easily customizable.

Skin Customizations
^^^^^^^^^^^^^^^^^^^

The most frequent customization will be on how links are displayed. Create a 
directory called ``social_bookmarking`` in your project's template directory. 
Then copy the HTML file ``social_bookmarking/templates/social_bookmarking/links.html`` 
to this project directory.

CSS customizations
^^^^^^^^^^^^^^^^^^

The following classes and IDS are attached to the skin::

    div.social-bookmarking
        span.bookmark #bookmark.title|slugify
        
Other classes and IDs will be assigned as requested by competent CSS designers.

Todo
-----

 * Add more social networking sites
 * Validation existing social networking sites. Sounds like a test to me!
 * Full suite of tests against each site stored in the fixture.
 * Maybe some caching stuff?

Other Django Social Bookmarking applications
--------------------------------------------

Django Social Bookmarking is a very rough fork of these two applications. 

 * `django-social-bookmarks <http://bitbucket.org/trbs/django-social-bookmarks/>`_
 
 * `django-sociable <http://bitbucket.org/kmike/django-sociable/>`_

