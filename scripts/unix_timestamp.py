import time
from sys import argv

from datetime import datetime

def main():
    month = int(raw_input('enter month XX: '))
    day = int(raw_input('enter day XX: '))
    year = int(raw_input('enter year XXXX: '))
    hour = int(raw_input('enter hour XX: '))
    minute = int(raw_input('enter minute XX: '))
    second = int(raw_input('enter second XX: '))

    actual = datetime(year, month, day, hour, minute, second)

    try:
        timestamp = int(time.mktime(actual.timetuple()))
        print('unix timestamp for {} is {}'.format(actual, timestamp))

    except:
        print('could not parse entered values')

if __name__ == '__main__':
    main()
