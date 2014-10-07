#! /usr/bin/env python

from pyethereum import tester as t
import sys
import re


def run_serpent():
    """Call a serpent (.se) contract on a test blockchain"""
    s = t.state()  #Initialize genesis block
    c = s.contract('namecoin.se')  #Initialize contract

    name = "george"
    locn = 45
    result = s.send(t.k0, c, 0, [[name, locn]])
    print "Claim name \"{}\"\n at location {}\n result = {}".format(name, locn, result)

    name = "george"
    locn = 20
    result = s.send(t.k0, c, 0, [[name, locn]])
    print "Claim name \"{}\"\n at location {}\n result = {}".format(name, locn, result)

    name = "harry"
    locn = 65
    result = s.send(t.k0, c, 0, [[name, locn]])
    print "Claim name \"{}\"\n at location {}\n result = {}".format(name, locn, result)


def main(args):
    """Parse command line options (TODO)"""
    run_serpent()


if __name__ == "__main__":
    main(sys.argv[1:])

