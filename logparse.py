
from sys import argv
from datetime import datetime
from math import ceil


def parse(log_file):
    lines = list()
    with open(log_file, 'r') as fp:
        for line in fp:
            line = line.strip()
            if 'Device State:' in line:
                timestamp = line[:19]
                state = line.split()[-1]
                if state in {'ON', 'OFF', 'ERR'}:
                    lines.append((state, timestamp))
    return lines


def calculate(lines):
    time_on = 0
    time_started = 0
    for state, timestamp in lines:
        if state == 'ERR':
            print('Error : {}'.format(timestamp))
        elif state == 'ON' and time_started == 0:
            time_started = datetime.strptime(timestamp, '%b %d %H:%M:%S:%f')
        elif time_started != 0:
            time_finished = datetime.strptime(timestamp, '%b %d %H:%M:%S:%f')
            time_diff = time_finished - time_started
            time_on += time_diff.total_seconds()
            time_started = 0
    return ceil(time_on)


def log_parse(log_file):
    lines = parse(log_file)
    time_on = calculate(lines)
    print('The device was left on for less than {} seconds.'.format(ceil(time_on)))


if __name__ == '__main__':
    log_parse(argv[1])
