#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
import time

if __name__ == '__main__':
    dev = Device(host='192.168.108.199', user='lab', passwd='lab123')
    dev.open()
    intfs = EthPortTable(dev)
    intfs.get()
    for intf in intfs:
        print "Data: Name %s, Desc %s, Mac %s" % (intf.key, intf.description, intf.macaddr)
    time.sleep(2)
    dev.close() 
