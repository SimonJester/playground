#! /usr/bin/env python

from pyethereum import tester as t
import sys
from runserpent import run_serpent
from runserpent import convert_args


def main():
    print run_serpent('mul2.se', convert_args(sys.argv[1:]))


if __name__ == "__main__":
    main()

