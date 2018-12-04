#!/usr/bin/env python
import itertools

inputfile = 'input'

def find_differences(s1, s2):
    difference = [i for i in xrange(len(s1)) if s1[i] != s2[i]]
    return difference

def compute_checksum(fp):
    two_chars = 0
    three_chars = 0
    for line in fp:
        d = {x:line.strip().count(x) for x in line.strip()}
        if 2 in d.values():
            two_chars += 1
        if 3 in d.values():
            three_chars += 1
    checksum = two_chars * three_chars
    return checksum

def find_smallest_diff(fp):
    lines = [line.strip() for line in fp]
    lowest = ()
    for a, b in itertools.combinations(lines, 2):
        output = find_differences(a, b)
        if not lowest:
            lowest = (len(output), a, b)
        elif len(output) < lowest[0]:
            lowest = (len(output), a, b)
    return lowest

def main():
    try:
        with open(inputfile) as fp:
            checksum = compute_checksum(fp)
            print "Checksum is %s" % checksum
            fp.seek(0)
            lowest = find_smallest_diff(fp)
            common = [c for c in lowest[1] if c in lowest[2]]
            print "Common boxID is %s" % ''.join(common)
    except IOError:
        print "Could not find input file"

if __name__ == "__main__":
    main()

