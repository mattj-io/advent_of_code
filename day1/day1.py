#!/usr/bin/env python
import re

inputfile = 'input'

def part1(fp):
    freq = 0
    for line in fp:
        num = line.strip()
        if re.search(r'-?\d+', num):
            freq += int(num)
        else:
            print "Failed input check %s" % num
            continue
    return freq

def part2(fp):
    freq = 0
    stored_freqs = []
    while True:
        for line in fp:
            num = line.strip()
            if re.search(r'-?\d+', num):
                freq += int(num)
                if freq in stored_freqs:
                    return freq
                else:
                    stored_freqs.append(freq)
            else:
                print "Failed input check %s" % num
                continue
        fp.seek(0)

def main():
    try:
        with open(inputfile) as fp:
            final_freq = part1(fp)
            print "Final frequency is %i" % final_freq
            repeat_freq = part2(fp)
            print "First duplicate frequency is %i" % repeat_freq
    except IOError:
        print "Could not find input file"

if __name__ == "__main__":
    main()
