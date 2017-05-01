from datetime import datetime
from sys import argv

def main():
    timestamp = argv[1]
    if not timestamp:
        print('please enter date as command line argument')
        return
        
    try:
        pretty = (datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        print(pretty)
    except:
        print('could not parse date')

if __name__ == '__main__':
    main()
