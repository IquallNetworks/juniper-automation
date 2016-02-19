#!/usr/bin/python

from lxml import etree
from jnpr.junos import Device

if __name__ == '__main__':
    dev = Device(host='192.168.108.199', user='jaut')
    dev.open()
    result = dev.rpc.ping(host="192.168.108.193", count="2")
    print etree.tostring(result)
    print "Fin!!"
    dev.close()
