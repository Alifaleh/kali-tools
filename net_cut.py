#!/user/bin/env python

import netfilterqueue

def queue_process(packet):
    print(packet)
    #packet.drop()
    packet.accept()

queue=netfilterqueue.NetfilterQueue()
queue.bind(1,queue_process)
queue.run()