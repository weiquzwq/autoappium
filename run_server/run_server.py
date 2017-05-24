import socket
import os
import time
import devices
import sys
import check_port
reload(sys)
sys.setdefaultencoding('utf-8')


iplist=[]
iplist = socket.gethostbyname_ex(socket.gethostname())
ip=iplist[2][0]
divlist=devices.get_devices()
print divlist
port=4723
bport=5723
conf="..\\conf\\appium_cf.json"

def check_ip_port(ipv,portv):
    if check_port.IsOpen(ipv,portv)==True:
        portv=portv+1
        return check_ip_port(ipv,portv)
    else: 
        return portv
           
        
for div in divlist:
    port=check_ip_port(ip,port)
    bport=check_ip_port(ip,bport)
    run_app='start run_appium.bat {0} {1} {2} {3} {4}'.format(ip,port,bport,div,conf)
    os.system(run_app)
    port=port+1
    bport=bport+1


time.sleep(5)
#cmd="start run_test.bat"
#os.system(cmd)
