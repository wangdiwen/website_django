#!/usr/bin/env python

# import django env
from django.conf.urls import patterns, include, url

# import web site modles
from controllers import home

# urls conf
urlpatterns = patterns('',  # init instance
    # web site urls
    url(r'^$', home.index),
    url(r'^test/$', home.test),

)
