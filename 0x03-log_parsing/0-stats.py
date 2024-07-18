#!/usr/bin/python3
"""
0-stats.py
"""
import sys


def formated_print(data):
    ''' prints data in fromated way '''
    out = "File size: {}\n".format(data['size'])
    for key in data['codes']:
        if data['codes'][key] != 0:
            out += '{}: {}\n'.format(key, data['codes'][key])
    sys.stdout.write(out)
    sys.stdout.flush()


def extract(data, line):
    ''' check if the input is valid and extracts data from it '''
    line = line.rsplit()
    try:
        status = line[-2]
        if status in data['codes']:
            data['codes'][status] += 1
        data['size'] += int(line[-1])
    except (IndexError, ValueError):
        pass


def main(data):
    ''' program entry level '''
    i = 0
    for line in sys.stdin:
        extract(data, line)
        i += 1
        if i % 10 == 0:
            formated_print(data)
    formated_print(data)


if __name__ == '__main__':
    data = {
        'size': 0, 'codes': {
            '200': 0, '301': 0,
            '400': 0, '401': 0, '403': 0,
            '404': 0, '405': 0, '500': 0
        }
    }

    try:
        main(data)
    except KeyboardInterrupt:
        formated_print(data)
        raise
