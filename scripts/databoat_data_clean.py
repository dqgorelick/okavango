#!/usr/bin/env python
import xmltodict
import math
import csv
from datetime import datetime
from sys import argv

from source_references import lakes, check_location


def readable_date(unix_timestamp):
    return datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%dT%H:%M:%SZ')


def main():
    selected = argv[1]

    if not check_location(selected):
        print('please source name listed in source_references')
        return

    transect_path = lakes[selected]['working_path']
    print(transect_path)
    output_path = lakes[selected]['output_path']

    # utc adjustment work
    recorded = lakes[selected]['time_adjustment_recorded']
    actual = lakes[selected]['time_adjustment_actual']
    diff = recorded - actual

    # check files exist and can be parsed
    try:
        ambit = xmltodict.parse(open(lakes[selected]['ambit_path']))
    except:
        print('cannot find or process ambit file path')
        return

    try:
        transect_data = csv.reader(open(transect_path))
    except:
        print('cannot find sensor-reading csv path')
        return

    # filter out all values in ambit data without long / lat
    valid_samples = []
    for sample in ambit['sml']['DeviceLog']['Samples']['Sample']:
        if sample.has_key('Longitude') and sample.has_key('Latitude'):
            for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ'):
                try:
                    sample.datetime = datetime.strptime(sample['UTC'], fmt)
                except ValueError:
                    pass
            if sample.datetime:
                valid_samples.append(sample)
            else:
                print ('cannot match format for ambit UTC value')
                return

    with open(output_path, 'w') as output:
        writer = csv.writer(output)
        for d in transect_data:
            # adjust unix timestamp if-need-be, otherwise leave it be
            print('pre-adjusted:{}'.format(readable_date(d[1])))
            d[1] = int(d[1]) - diff
            print('adjusted:{}'.format(readable_date(d[1])))

            # find watch UTC value which is closest to unix timestamp adte
            timestamp = datetime.fromtimestamp(int(d[1]))
            min_delta = abs(timestamp - datetime.max)
            for sample in valid_samples:
                if abs(sample.datetime - timestamp) < min_delta:
                    min_delta = abs(sample.datetime - timestamp)
                    closest_time = sample

            d.append(readable_date(d[1]))
            d.append(str(math.degrees(float(closest_time['Latitude']))))
            d.append(str(math.degrees(float(closest_time['Longitude']))))

            print('writing row: {}'.format(d))
            writer.writerow(d)

if __name__ == '__main__':
    main()
