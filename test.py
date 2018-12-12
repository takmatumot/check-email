#/usr/bin/env python
"""
  test script to check email
"""

__author__ = "Takahiro Matsumoto"
__date__ = "2018-12-11"


import util

if __name__ == "__main__":

    print("### test to check email ###")

    valid_email = "xxx@xxx.xx.jp"
    print("valid_email = ", valid_email, ", result=", util.check_email(valid_email))

    invalid_email = "xxx@xxx.xx.jp."
    print("invalid_email = ", invalid_email, ", result=", util.check_email(invalid_email))



