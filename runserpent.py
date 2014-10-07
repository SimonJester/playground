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


def run_contract(contract, parms):
    s = t.state()  #Initialize a genesis block
    c = s.contract(contract)
    return s.send(t.k0, c, 0, [parms])


def main(args):
    """Parse command line options (TODO)"""
    print run_contract(args[0], [convert_arg(val) for val in args[1:]])


if __name__ == "__main__":
    main(sys.argv[1:])

