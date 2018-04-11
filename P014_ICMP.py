import socket,os
import pyping
import datetime
import time

def gcdt():
    GCDT = datetime.datetime.now()
    return GCDT

def hostAddr():
    GCDT=gcdt()
    hostName=raw_input("[{}] Input Website or ip address:".format(GCDT))
    return hostName

def py_ping(HN):
    GCDT = gcdt()
    r=pyping.ping(HN)
    if r.avg_rtt=="None":
        print("[{}] This Host doesn't exist".format(GCDT))
    else:
        print("[{}] Avg. Round Trip Time={} ms from here to {}".format(GCDT, r.avg_rtt, HN))
        #r = pyping.ping("192.168.1.185")
        #if r.ret_code==0:
        #    print("success\n")
        #else:
        #    print("unable to connect.\n")
        #print(r.ret_code,"\n")

        #print(r.destination_ip, "\n")

def main():
    GCDT = gcdt()
    HN=hostAddr()
    while(1):
        try:
            py_ping(HN)
        except KeyboardInterrupt:
            print("[{}] Keyboard Interrupted.".format(GCDT))
            HN = hostAddr()
            py_ping(HN)
        except:
            print("[{}] unable to connect to the {}.".format(GCDT,HN))
            HN = hostAddr()
            py_ping(HN)


# script starts here
main()
