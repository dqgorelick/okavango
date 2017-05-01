#!/usr/bin/env python
import csv
import json
import urllib2
from sys import argv
from source_references import lakes, check_location, columns


def main():
    selected = argv[1]

    if not check_location(selected):
        print('please source name listed in source_references')
        return

    req = urllib2.Request('http://23.23.124.78/ingest/databoat')
    req.add_header('Content-Type', 'application/json')

    data_path = lakes[selected]['output_path']

    try:
        transect_data = csv.reader(open(data_path))
    except:
        print('cannot find sensor reading csv path')

    data = []
    for it, row in enumerate(transect_data):
        data.append({
            'SourceLake': lakes[selected]['source_name'],
            'Expedition': 'source_17',
            'MeasurementMethod': lakes[selected]['measurement_method']
        })
        for i, d in enumerate(row):
            if columns[i] != 'skip':
                data[it][columns[i]] = d

    print(json.dumps(data))
    
    upload = raw_input('Upload data? (y/N): ')
    if upload == 'y':
        try:
            response = urllib2.urlopen(req, json.dumps(data))
            print('uploaded! code: {}, message: {}'.format(response.code, response.read()))
        except urllib2.HTTPError, e:
            print('error uploading data... code: {}, message: {}'.format(e.code, e.read()))
            
    else: 
        print('not uploading!')
    

if __name__ == '__main__':
    main()
