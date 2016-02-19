#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.op.arp import ArpTable
import time

def procedimiento_arp(ip, user, passwd):
    print "Tabla ARP para host %s" % ip
    dev = Device(host=ip, user=user, passwd=passwd)
    dev.open()
    arp_list = ArpTable(dev)
    arp_list.get()
    for arp_elem in arp_list:
        print " arp %s asociada a ip %s por interfaz %s" % (arp_elem.mac_address, arp_elem.ip_address, arp_elem.interface_name)
    print "\n"    
    time.sleep(2)
    dev.close()
    
if __name__ == '__main__':
    procedimiento_arp('192.168.108.199', 'lab', 'lab123')
    procedimiento_arp('192.168.108.200', 'lab', 'lab123')
    
