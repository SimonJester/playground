#! /usr/bin/env python

import sys
from runserpent import run_serpent


def main():
    print run_serpent('mul2.se', sys.argv[1:], convert_to_int=True)


if __name__ == "__main__":
    main()

