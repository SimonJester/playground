#!/usr/bin/env python

# This is an example of something you normally do NOT want to do:
# defining the default value of the parameter as a mutable object
# (in this case a list).
#
# The way this code behaves is as follows:
# The FIRST TIME the function is called in a way that assigns the 
# default value to the parameter is when the mutable list is defined.
# Any subsequent call that does NOT provide the optional parameter 
# will re-use the original mutable list.
# Any subsequent call that DOES provide the optional parameter 
# will NOT use the origianal mutable list.


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2, []))
print(f(3))
