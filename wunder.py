#!/usr/bin/env python

"""
Retrieves weather data from Weather Underground
historical data service
"""

import argparse
import requests
import re
from datetime import datetime

def wudata(station, start_date=None, end_date=None, clean=True):
    URL_TPL = (
        'https://www.wunderground.com/'
        'history/'
        'airport/{station}/'
        '{start_year}/{start_month}/{start_day}/'
        'CustomHistory.html'
        '?yearend={end_year}'
        '&monthend={end_month}'
        '&dayend={end_day}'
        '&format=1'
    )
    
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    else:
        start_date = datetime.today()

    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    else:
        end_date = datetime.today()

    URL = URL_TPL.format(
        station     = station,
        start_year  = start_date.year,
        start_month = start_date.month,
        start_day   = start_date.day,
        end_year    = end_date.year,
        end_month   = end_date.month,
        end_day     = end_date.day
    )

    data = None

    r = requests.get(URL)
    if r.ok:
        data = r.text

        if clean:
            # cleanup: remove unnecessary <br/> tags, and leading blank line
            data = re.sub('\<br /\>', '', data)
            data = re.sub('^\n', '', data)

    else:
        print('Error retrieving data. Returned {}'.format(r.status_code))

    return(data)

parser = argparse.ArgumentParser()
parser.add_argument('station', type=str, help='weather station code')
parser.add_argument('-s', '--start-date', type=str, help='start date')
parser.add_argument('-e', '--end-date', type=str, help='end date')
parser.add_argument('-y', '--year', type=str, help='data year')
parser.add_argument('-r', '--raw', dest='clean', action='store_false')

if __name__ == '__main__':
    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date

    if args.year:
        # collect a full years worth of data
        start_date = '{}-01-01'.format(args.year)
        end_date = '{}-12-31'.format(args.year)
    
    clean = args.clean

    print(wudata(args.station, start_date, end_date, clean))

