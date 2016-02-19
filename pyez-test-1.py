#!/usr/bin/python

from jnpr.junos import Device

if __name__ == '__main__':
    dev = Device(host='192.168.108.199', user='jaut')
    dev.open()
    xx = dev.rpc.get_software_information()
    print "Version de soft: %s" % xx.findtext('junos-version').strip()
    dev.close()
