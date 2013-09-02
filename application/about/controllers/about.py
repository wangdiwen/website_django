#!/usr/bin/env python

# import python env
import os
import sys

# import django env
from django.http import HttpResponse
# from django.shortcuts import render_to_response

def test(request):
    msg = 'about test'
    return HttpResponse(msg)
