#!/usr/bin/env python

# import python env
import os
import sys

# import django env
from django.http import HttpResponse
from django.shortcuts import render_to_response

# import define helpers env
# from helpers import util_tool

# import define libs env
# from libs import mylib

###############################################################################
# examples below
###############################################################################
def index(request):
    template_name = 'templates/backend/home.html'
    data = {'name': 'diwen'}
    return render_to_response(template_name, data)

def test(request):
    msg = 'backend test'
    return HttpResponse(msg)
###############################################################################
