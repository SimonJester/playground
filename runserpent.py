#! /usr/bin/env python

from pyethereum import tester as t
import sys
import re


def convert_arg(arg):
    """Convert a single argument to integer if it's all digits"""
    if re.match('^\d+$', arg, re.DOTALL):
        return int(arg)
    else:
        return arg

def convert_args(args):
    """Convert a list of arguments to integer 
    but only if the arg is all digits"""
    return [convert_arg(val) for val in args]


def run_serpent(contract, parms, convert_to_int=False):
    """Call a serpent (.se) contract on a test blockchain"""
    if convert_to_int:
        args = convert_args(parms)
    else:
        args = parms
    s = t.state()  #Initialize a genesis block
    c = s.contract(contract)
    return s.send(t.k0, c, 0, [args])


def print_usage():
    print "Usage:"
    print "    runserpent.py <serpent-contract-name> <contract-parameters>"
    print ""


def main(args):
    """Parse command line options (TODO)"""
    try:
        print run_serpent(args[0], args[1:], convert_to_int=True)
    except IndexError:
        print_usage()


if __name__ == "__main__":
    main(sys.argv[1:])

