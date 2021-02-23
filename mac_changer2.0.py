#!/usr/bin/env python

import subprocess
import time

print('--------------------------------------------------------------------------------\n                              Welcome to mac_changer2.0\n                                  by:Ali-A.faleh\n\n')



interface=str(raw_input("Enter the Interface Name :"))
mac=str(raw_input("Enter the New MAC Address => "))

print('\n\n[+] Changing the Interface '+interface+' MAC Address to => '+mac)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', mac])
subprocess.call(['ifconfig', interface, 'up'])
print('\n\n[+] '+interface+' MAC Address has been changed successfuly to => '+mac)
time.sleep(3)
raw_input('\n\nPress ENTER to show the ifconfig')
subprocess.call('ifconfig',shell=True)
