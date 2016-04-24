
import os
import sys

command = sys.argv
if len(command) == 2:
    os.system("python img2iqstream -s 1000000 -l 1 -o bladerf.iq --format bladerf %s" % command[1])

os.system("bladerf-cli -s bladerf.script")


