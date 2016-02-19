#!/usr/bin/python

'''
Script para hacer un shutdown en 5 minutos 
'''

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
import time

if __name__ == '__main__':
    dev = Device(host='192.168.108.199', user='lab', passwd='lab123')
    dev.open()
    mi_sw = SW(dev)
    print mi_sw.poweroff(5)
    print "Fin del script.."
    time.sleep(2)
    dev.close()
