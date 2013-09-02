#!/usr/bin/env python

# import django env
from django.conf.urls import patterns, include, url

# import web site modles
from controllers import home

# urls conf
urlpatterns = patterns('',  # init instance
    # web site urls:
    # example below
    url(r'^$', home.index),
    url(r'^index/$', home.index),
    url(r'^test/$', home.test),
    url(r'^hello/(.*)/$', home.hello),
    url(r'^ajax/$', home.ajax),
    url(r'^test_helper$', home.test_helper),
    url(r'^test_lib$', home.test_lib),
    url(r'^test_db/$', home.my_table),

)
