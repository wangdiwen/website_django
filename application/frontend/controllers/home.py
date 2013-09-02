#!/usr/bin/env python
#coding=utf-8

# import python env
import os
import sys
import json

# import django env
from django.http import HttpResponse
from django.shortcuts import render_to_response

# import define helpers env
from helpers.util_tool import *
# import define libs env
from libs import mylib

# import the db module
from frontend.models.my_table import My_my_table

###############################################################################
# examples below
###############################################################################
def my_table(request):
    template_name = 'templates/frontend/my_table.html'
    obj = My_my_table()

    # insert to db
    # ret = obj.insert_one('王地文', '24', '1', 'Keep it simple & stupid.')

    # del one record
    # ret = obj.delete_one(6)

    # update one record
    # ret = obj.update_one(5, 'fish')

    # check has one record
    # id = 4
    # ret = obj.has_one(id)
    # if not ret:
    #     print 'Oh, not exist id = %s' % id
    # else:
    #     print 'Ok, exist id = %s' % id

    # check has name record
    # ret = obj.has_one_by_name('地文')
    # if ret:
    #     echo('has name')
    # else:
    #     echo('no name')

    query = obj.get_by_id(6)
    # query = obj.get_all()
    # query = 'I love U, my lady'

    # test data
    ret = echo_json(query)
    return HttpResponse(ret)

    # return HttpResponse('测试一下中文')
    return render_to_response(template_name, {'personal': query})

###############################################################################
def index(request):
    template_name = 'templates/frontend/home.html'
    data = {'name': 'diwen'}
    return render_to_response(template_name, data)

def test(request):
    # msg = 'frontend test'
    var = {
        'name': 'diwen',
        'sex': 'man',
        'age': '24',
        # 'hobby': 'read',
    }
    msg = json.dumps(var)
    return HttpResponse(msg)

def hello(request, name = ''):
    template_name = 'templates/frontend/home.html'
    data = {'name': name}
    return render_to_response(template_name, data)

def ajax(request):
    return HttpResponse('ajax value')

def test_helper(request):
    context = util_tool.test()
    return HttpResponse(context)

def test_lib(request):
    name_obj = mylib.MyName('diwen')  # class instanse
    my_name = name_obj.get_name()
    return HttpResponse(my_name)
###############################################################################
