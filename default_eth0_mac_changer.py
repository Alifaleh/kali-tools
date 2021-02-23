#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down",shell=True)
subprocess.call("ifconfig eth0 hw ether 08:00:27:be:0c:78",shell=True)
subprocess.call("ifconfig eth0 up",shell=True)
