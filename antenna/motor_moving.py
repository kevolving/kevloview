import smbus
import time
import os
import sys
import subprocess
import datetime

bus = smbus.SMBus(0x01)
addr = 0x04

def dmotor(time, flag, cpos):    
    now = datetime.datetime.now()    
    if flag == 0:
        tmphour = time / 60
        tmpmin = time % 60
        os.system('sh calcSpecifiedTimePosISS.sh "%s %s %s %s %s 0" %s,%s,%s > res' % (now.year, now.month, now.day, now.hour + tmphour, tmpmin, cpos[0], cpos[1], cpos[2]))    
    else:
        os.system('sh calcSpecifiedTimePosISS.sh "%s %s %s %s %s %s" %s,%s,%s > res' % (now.year, now.month, now.day, now.hour, now.minutes, now.seconds, cpos[0], cpos[1], cpos[2]))
        

    f = file("res")
    res = f.readlines()
    elems = res[1].split(",")
    try:
        az = elems[6].split("+")[1]
        el = elems[7]
        if(el.find("-")==-1):
            el = el.split("+")[1]

        az = float(az)
        el = float(el)
        if(az > 180):
            az = az - 180
            el = el + 90
        
        bus.write_i2c_block_data(addr, 0x01, [int(float(az)), int(float(el))])
        time.sleep(0.05)
    except:
        {}
        
commands = sys.argv

if(len(sys.argv) == 2):
    if(sys.argv[1] == "cal"):
        for i in range(0, 180, 5):
            bus.write_i2c_block_data(addr, 0x01, [int(float(i)), int(float(0))])
            time.sleep(0.1)
        bus.write_i2c_block_data(addr, 0x01, [int(float(0)), int(float(0))])
        time.sleep(0.5)
        for i in range(0, 180, 5):
            bus.write_i2c_block_data(addr, 0x01, [int(float(0)), int(float(i))])
            time.sleep(0.1)
        bus.write_i2c_block_data(addr, 0x01, [int(float(0)), int(float(0))])
        time.sleep(1)
        for i in range(0, 180, 5):
            bus.write_i2c_block_data(addr, 0x01, [int(float(i)), int(float(i))])
            time.sleep(0.1)
        bus.write_i2c_block_data(addr, 0x01, [int(float(0)), int(float(0))])
        time.sleep(1)
        
        exit(1)
    elif(sys.argv[1] == "demo"):
        for i in range(60):
            dmotor(i, 0, [35.6, 137, 10])
            time.sleep(0.1)        

for i in range(600):
    dmotor(i, 1, [35.6, 137, 10])
    time.sleep(0.1)
    

    
