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
 
Todo
-----

 * Installation documentation
 * Usage documentation
 * Internationalization!
 * Add more social networking sites
 * Validation existing social networking sites. Sounds like a test to me!
 * Full suite of tests against each site stored in the fixture.


Other Django Social Bookmarking applications
--------------------------------------------

Django Social Bookmarking is a very rough fork of these two applications. 

 * `django-social-bookmarks <http://bitbucket.org/trbs/django-social-bookmarks/>`_
 
 * `django-sociable <http://bitbucket.org/kmike/django-sociable/>`_

