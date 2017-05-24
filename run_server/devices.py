#coding=utf-8
import threading
from time import ctime,sleep
import os 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_devices():
    #run_grid="adb kill-server "
    #os.system(run_grid)
    output=os.popen("adb devices").readlines()
    deviceslist=output[1:len(output)-1]
    devices=[]
    for device in deviceslist:
        dev=device.split('\t')[0]
        devices.append(dev)
    return devices

