from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
=====================================================
django-social-bookmarking (Django Social Bookmarking)
=====================================================
 
Django Social Bookmarking provides links to various bookmarking 
engines such as Digg, Reddit, Yahoo, etc. Control over which bookmarks
are used is done via the admin interface. This package is properly 
eggified and is licensed under the MIT/BSD license.
"""
 
setup(
    name='django-social-bookmarking',
    version=version,
    description="Django Social Bookmarking",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='social,bookmarks,django',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-social-bookmarking/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools_git'],
)