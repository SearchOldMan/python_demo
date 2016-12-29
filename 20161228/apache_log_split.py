#!/usr/bin/env python

import sys

def dic_log_line(line):
    split_line = line.split()
    return {'remote_host:':split_line[0],'status':split_line[7],'bytes_len':split_line[8]}

def generate_log_report(logfile):
    report_dict = {}
    for line in logfile:
        line_dict = dic_log_line(line)
        print line_dict
        try:
            bytes_len = int(line_dict['bytes_len'])
        except ValueError:
            continue
        report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_len)

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print __doc__
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name,'r').read()
    except:
        print 'filename is not such'

    generate_log_report(infile)