#!/usr/bin/env python
import re
freq = 0
inputfile = 'input'
try:
    with open(inputfile) as fp:
        for line in fp:
            num = line.strip()
            if re.search(r'-?\d+', num):
                freq += int(num)
            else:
                print "Failed input check %s" % num
                continue
    print "Frequency is %i" % freq
    fp.close()
except IOError:
    print "Could not find input file"
