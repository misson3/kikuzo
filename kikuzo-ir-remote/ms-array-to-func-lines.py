# Feb 25, 2024, ms
# ms-array-to-func-lines.py

"""
1. get raw signal patterns with ReceiveDamp exmple in the IRremote
2. save the duration pair line into a file and feed it to this code
3. this code generates pulse(); delayMicoroseconds(); lines to the STDOUT
4. save the lines in a function and call to send IR command
"""

import sys


def parse_sig_line(array_txt):
    # hl_tuples = [(high, low),,, (high,)]
    with open(array_txt, mode='r') as IN:
        for line in IN:
            line = line.rstrip()
            if line[0].isdigit():
                hls = line.split(', ')  # list of 'h,l'. last would be only h
                hl_tuples = [tuple(hl.split(',')) for hl in hls[:-1]]
                # add the last high with dummy low
                hl_tuples.append((hls[-1], '1000'))
    return hl_tuples


def print_in_func(tuple_list):
    """
    just put (high, low) in
    pulseIR(high);
    delayMicroseconds(low);
    """
    for h, l in tuple_list:
        print(f'pulseIR({h});')
        print(f'delayMicroseconds({l});')


def mainstory(array_txt):
    # read data line from array_txt
    durations = parse_sig_line(array_txt)
    # print(durations)

    # put high, low in
    # pulseIR(high);
    # delayMicroseconds(low);
    print_in_func(durations)


if __name__ == '__main__':
    array_txt = sys.argv[1]
    mainstory(array_txt)
