from django.conf.urls.defaults import *



urlpatterns = patterns('',
    url(r'^$', "test_app.views.index", name='index'),    

    
    )