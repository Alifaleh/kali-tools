#!/usr/bin/env python

import subprocess
import time
import optparse



parser=optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='used to enter the interface.')
parser.add_option('-m', '--mac', dest='new_mac', help='used to enter the new mac.')

(options,arguments)=parser.parse_args()

interface=str(options.interface)
mac=str(options.new_mac)

print('\n\n[+] Changing the Interface '+interface+' MAC Address to => '+mac)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
subprocess.call(['ifconfig', interface, 'up'])
print('\n\n[+] '+interface+' MAC Address has been changed successfuly to => '+mac)
time.sleep(3)
raw_input('\n\nPress ENTER to show the ifconfig')
subprocess.call('ifconfig',shell=True)
