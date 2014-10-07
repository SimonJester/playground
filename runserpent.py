#! /usr/bin/env python

from pyethereum import tester as t
import sys
import re


def convert_arg(arg):
    """Convert argument to integer if it's all digits"""
    if re.match('^\d+$', arg, re.DOTALL):
        return int(arg)
    else:
        return arg

def convert_args(args):
    return [convert_arg(val) for val in args]


def run_serpent(contract, parms):
    s = t.state()  #Initialize a genesis block
    c = s.contract(contract)
    return s.send(t.k0, c, 0, [parms])


def print_usage():
    print "Usage:"
    print "    runserpent.py <serpent-contract-name> <contract-parameters>"
    print ""


def main(args):
    """Parse command line options (TODO)"""
    try:
        print run_serpent(args[0], convert_args(args[1:]))
    except IndexError:
        print_usage()


if __name__ == "__main__":
    main(sys.argv[1:])

