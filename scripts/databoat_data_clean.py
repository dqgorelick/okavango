#!/usr/bin/env python
import xmltodict
import csv
from datetime import datetime

# change paths to link different data sets
ambit_path = '../databoat/ambit_data.sml'
transect_path = '../databoat/cuanavale_transect.CSV'
output_path = '../databoat/cuanavale_transect_combined.csv'


def main():
    try:
        ambit = xmltodict.parse(open(ambit_path))
    except:
        print('cannot find ambit file path')

    valid_samples = []
    for sample in ambit['sml']['DeviceLog']['Samples']['Sample']:
        if sample.has_key('Longitude') and sample.has_key('Latitude'):
            for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ'):
                try:
                    sample.datetime = datetime.strptime(sample['UTC'], fmt)
                except ValueError:
                    pass
            valid_samples.append(sample)
    try:
        transect_data = csv.reader(open(transect_path))
    except:
        print('cannot find sensor reading csv path')

    with open(output_path, 'w') as output:
        writer = csv.writer(output)
        for d in transect_data:
            timestamp = datetime.fromtimestamp(int(d[1]))
            min_delta = abs(timestamp - datetime.max)
            for sample in valid_samples:
                if abs(sample.datetime - timestamp) < min_delta:
                    min_delta = abs(sample.datetime - timestamp)
                    closest_time = sample

            d.append(str(closest_time['Latitude']))
            d.append(str(closest_time['Longitude']))

            print('sample time: {}'.format(timestamp))
            print('writing row: {}'.format(d))
            writer.writerow(d)

if __name__ == '__main__':
    main()
