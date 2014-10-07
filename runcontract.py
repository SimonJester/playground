#! /usr/bin/env python

from pyethereum import tester as t
import sys


def run_contract(contract, args):
    s = t.state()  #Initialize a genesis block
    c = s.contract(contract)
    return s.send(t.k0, c, 0, [args])


def main(args):
    """Parse command line options (TODO)"""
    print run_contract(args[0], [int(val) for val in args[1:]])


if __name__ == "__main__":
    main(sys.argv[1:])

