#!/usr/bin/env python
import os
import sys

###############################################################################
class MyName(object):
    """docstring for MyName"""

    def __init__(self, name):
        super(MyName, self).__init__()
        self.name = name

    def get_name(self):
        return self.name
