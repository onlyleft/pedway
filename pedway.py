#!/usr/bin/env python3
import argparse
import findTime

def add(args):
    specDate = findTime.findDay(a.day)
    print("Recording {steps:,} steps on {date}".format(steps = a.steps, date=specDate))

def update(args):
    specDate = findTime.findDay(a.day)
    print("Changing {date} to {steps:,} steps".format(steps = a.steps, date=specDate))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pedway")
    subParsers = parser.add_subparsers()

    parentParser = argparse.ArgumentParser(add_help=False)
    parentParser.add_argument("--day", "-d", nargs="+", default=[], type=int)

    addParser = subParsers.add_parser("add", parents=[parentParser])
    addParser.add_argument("steps",type=int)
    addParser.set_defaults(func=add)

    updateParser = subParsers.add_parser("update", parents=[parentParser])
    updateParser.add_argument("steps",type=int)
    updateParser.set_defaults(func=update)

    a = parser.parse_args()
    a.func(a)
