#!/usr/bin/env python

import subprocess
import time
import optparse


def change_mac(interface, mac):
    print('\n\n[+] Changing the Interface ' + interface + ' MAC Address to => ' + mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
    subprocess.call(['ifconfig', interface, 'up'])
    time.sleep(3)
    print('\n\n[+] ' + interface + ' MAC Address has been changed successfuly to => ' + mac)



def get_inter_mac():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='used to enter the interface.')
    parser.add_option('-m', '--mac', dest='new_mac', help='used to enter the new mac.')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Error.please enter an interface name.use --help for more info")
    if not options.new_mac:
        parser.error("[-] Error.please enter a MAC address.use --help for more info")
    return options


options= get_inter_mac()
change_mac(options.interface, options.new_mac)