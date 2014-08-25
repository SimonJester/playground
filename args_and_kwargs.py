#!/usr/bin/env python

from __future__ import print_function

def make_api_call(foo, bar, baz, *args, **kwargs):
    # "args" stands for arguments
    for a in args:
        print(a)
    print("---")

    # "kwargs" stands for keyword arguments
    for a in kwargs:
        print(a, kwargs[a])
    print("===")

make_api_call(1, 2, 3)
make_api_call(1, 2, 3, 4)
make_api_call(1, 2, 3, 5, 6)
make_api_call(1, 2, 3, abc=7)
make_api_call(1, 2, 3, ef=8, ghi=9)
