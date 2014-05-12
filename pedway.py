#!/usr/bin/env python3
import argparse
import findTime
import backend

def add(args):
    specDate = findTime.findDay(args.day)
    print("Recording {steps:,} steps on {date}".format(steps = a.steps, date=specDate))

def update(args):
    specDate = findTime.findDay(args.day)
    print("Changing {date} to {steps:,} steps walked".format(steps = a.steps, date=specDate))

def reset(args):
    specDate = findTime.findDay(args.day)
    answer = input("Are you sure you want to reset {day}? [no] ".format(day=specDate))
    if answer == "yes" or answer == "y":
        print("Resetting walked steps on {day}.".format(day=specDate))
        backend.reset(specDate)
    else:
        print("Okay then. I won't reset {day}".format(day=specDate))

def install(args):
    print("Checking for install at {path}".format(path=a.path))
    if not backend.is_installed(a.path):
        print("Setting up new database")
        backend.init_db(args.path)
    else:
        print("The database is already setup")

def config(args):
    parameters = args.params
    if len(parameters) == 0:
        print("Here's your current configuration:")
    elif len(parameters) == 1:
        currentValue = backend.get_config(parameters[0])
        print("'{key}' is currently '{value}'".format(key=parameters[0],value=currentValue))
    else:
        print("Setting {key} to {value}".format(key=parameters[0],value=parameters[1]))

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

    resetParser = subParsers.add_parser("reset", parents=[parentParser])
    resetParser.set_defaults(func=reset)

    installParser = subParsers.add_parser("install", parents=[parentParser])
    installParser.add_argument("--path", "-p", default="~/.pedway")
    installParser.set_defaults(func=install)

    configParser = subParsers.add_parser("config", parents=[parentParser])
    configParser.add_argument("params", nargs="*", default=[])
    configParser.set_defaults(func=config)

    a = parser.parse_args()
    if hasattr(a,"func"):
        a.func(a)
    else:
        parser.print_help()
