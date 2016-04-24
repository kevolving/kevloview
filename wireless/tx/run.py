
import os
import sys

command = sys.argv


if len(command) == 2:
    if(command[1] == "test"):
        os.system("python img2iqstream.py -s 1000000 -l 0.005 -o bladerf.iq --format bladerf sample.jpg")
    else:
        os.system("python img2iqstream.py -s 1000000 -l 0.005 -o bladerf.iq --format bladerf %s" % command[1])
        os.system("bladerf-cli -s bladerf.script")
else:
    print ""
    print "run [image filename]"
    print ""



