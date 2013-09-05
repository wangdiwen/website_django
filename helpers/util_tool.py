#!/usr/bin/env python
import os
import sys
import json
import re
import datetime
import collections

from django.http import HttpResponse

###############################################################################
###############################################################################
def echo(msg = ''):  # color print
    GREEN = '\033[32m'
    END = '\033[0m'
    print GREEN + msg + END
###############################################################################
def echo_json(query_set):
    data = {
        'Length': 0,
        'Query_data': [],
    }
    # print str(type(query_set))
    if query_set:
        if type(query_set) == list:
            for item in query_set:
                tmp_dict = {}
                for key in item.keys():
                    if type(item[key]) == datetime.datetime:
                        tmp_dict[key] = item[key].strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        tmp_dict[key] = item[key]
                if tmp_dict:
                    data['Query_data'].append(tmp_dict)
        elif type(query_set) == dict:
            data['Query_data'].append(query_set)
        elif type(query_set) == str:
            data['Query_data'].append(query_set)
        elif re.compile('.*ValuesQuerySet.*').match(str(type(query_set))):
            if isinstance(query_set, collections.Iterable):
                for item in query_set:
                    tmp_dict = {}
                    for key in item.keys():
                        if type(item[key]) == datetime.datetime:
                            tmp_dict[key] = item[key].strftime('%Y-%m-%d %H:%M:%S')
                        else:
                            tmp_dict[key] = item[key]
                    if tmp_dict:
                        data['Query_data'].append(tmp_dict)
        else:
            data['Query_data'].append('Holy Shit @_@')
            data['Query_data'].append('Don not use model get()/all() function !')
            data['Query_data'].append('We just support ValuesQuerySet object !')
            data['Query_data'].append('Pls use filter().values() in your db model !')
            data['Query_data'].append('Good Luck ^_^')
        data['Length'] = len(data['Query_data'])
    return "<pre>"+json.dumps(data, indent=4)+"</pre>"
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
