#!/usr/bin/python

'''
Script para hacer un cambio de hosntame
'''

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import time

if __name__ == '__main__':
    dev = Device(host='192.168.108.199', user='jaut')
    dev.open()
    mi_cfg = Config(dev)
    mi_cfg.load(path="config_set.set")
    mi_cfg.commit(confirm=2)
    time.sleep(2)
    dev.close()
