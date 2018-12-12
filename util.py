"""
  Utilities
"""

__author__ = "Takahiro Matsumoto"
__date__ = "2018-12-11"


import re

re_pattern_email =  re.compile("^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")

def check_email(val):
    if re_pattern_email.match(val):
        return True
    else:
        return False


