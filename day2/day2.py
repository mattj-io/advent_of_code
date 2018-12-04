#!/usr/bin/env python
import collections

inputfile = 'input'

def main():
    try:
        with open(inputfile) as fp:
            two_chars = 0
            three_chars = 0
            for line in fp:
                d = {x:line.strip().count(x) for x in line.strip()}
                if 2 in d.values():
                    two_chars += 1
                if 3 in d.values():
                    three_chars += 1
            checksum = two_chars * three_chars
            print "Checksum is %i" % checksum
    except IOError:
        print "Could not find input file"

if __name__ == "__main__":
    main()

