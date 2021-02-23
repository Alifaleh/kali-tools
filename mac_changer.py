#!/usr/bin/env python3

import subprocess

print('----------------------------------------------------------------------\n          Welcome to mac_changer\n              by:Ali-faleh\n\n')



interface=str(input("enter the interface name :"))
mac=str(input("enter the new mac address :"))

com1='sudo ifconfig '
com1+=interface
com1+=' down'

com2='sudo ifconfig '
com2+=interface
com2+=' hw ether '
com2+=mac

com3='sudo ifconfig '
com3+=interface
com3+=' up'

subprocess.call(com1,shell=True)
subprocess.call(com2,shell=True)
subprocess.call(com3,shell=True)
