#!/usr/bin/env python
#coding=utf-8

# import python env
import os
import sys
import json
import datetime

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

    # query = obj.get_by_id(6)
    # query = obj.get_all()
    # query = 'I love U, my lady'

    # test message table
    # ret = obj.live_message(3, 4, 'user 3 -> user 4 live message...', datetime.datetime.now())

    query = obj.get_all_msg()
    user_id_list = []
    usered_id_list = []
    if query:
        for item in query:
            user_id = item['msg_user_id']
            usered_id = item['msg_usered_id']
            if user_id > 0:
                # print user_id
                user_id_list.append(user_id)
                usered_id_list.append(usered_id)

    data = []
    ret_user = obj.get_user_name_by_id_list(list(set(user_id_list)))
    ret_usered = obj.get_user_name_by_id_list(list(set(usered_id_list)))
    if ret_user and ret_usered:
        for item in query:
            user_id = item['msg_user_id']
            usered_id = item['msg_usered_id']
            item['msg_user_name'] = ''
            item['msg_usered_name'] = ''

            for user in ret_user:
                if user['my_id'] == user_id:
                    item['msg_user_name'] = user['my_name']
                    break
            for usered in ret_usered:
                if usered['my_id'] == usered_id:
                    item['msg_usered_name'] = usered['my_name']
                    break
            data.append(item)
    return HttpResponse(echo_json(data))

    # test data
    return HttpResponse(echo_json(query))

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
