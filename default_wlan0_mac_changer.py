#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down",shell=True)
subprocess.call("ifconfig wlan0 hw ether ce:bc:ec:51:b0:21",shell=True)
subprocess.call("ifconfig wlan0 up",shell=True)
