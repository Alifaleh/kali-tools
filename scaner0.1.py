#!/usr/bin/env python

import scapy.all as scapy
import optparse
import subprocess

def scan (ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast=broadcast/arp_request
    answered, unanswered=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)
    print('IP\t\t\tMAC\n-----------------------------------------------------------------------')
    for elements in answered:
        print(elements[1].psrc +'\t\t'+ elements[1].hwsrc)

def parse():
    parser=optparse.OptionParser()
    parser.add_option('-r', '--range', dest='range', help='the range of IP address you want to scan.')
    (options,arguments)=parser.parse_args()
    if options.range:
        return options.range
    else:
        parser.error('[-] Error.try using --help for more info')


ip=parse()
scan(ip)