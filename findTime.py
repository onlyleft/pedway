#!/usr/bin/env python3
from datetime import date

def findDay(args):
    today = date.today()
    if len(args) == 0:
        return today

    if len(args) >= 3:
        year = args[2]
        if year > today.year:
            raise ValueError("Date cannot be in the future")
    else:
        year = today.year
    
    if len(args) >= 2:
        month = args[1]
        if month > today.month and year == today.year and len(args) <= 2:
            year = year - 1
    else:
        month = today.month

    if len(args) >= 1:
        day = args[0]
        if day >= today.day and month == today.month and len(args) <= 1:
            month = month -1
    else:
        day = today.day

    return date(year, month, day)



if __name__ == "__main__":
    print("Today is {today}".format(today=date.today().isoformat()))
    print(findDay([19,1,2013]))
    print(findDay([20,1]))
    print(findDay([1]))
    print(findDay([6,6]))
