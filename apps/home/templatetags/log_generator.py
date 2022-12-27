import csv
import random
import time
import pyshark
from datetime import  datetime


filed_name = ["time", "ip_source", "ip_dest", "protocol"]



with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=filed_name)
    csv_writer.writeheader()



networkInterface = "Wi-Fi"

# define capture object
capture = pyshark.LiveCapture(interface=networkInterface)

print("listening on %s" % networkInterface)

for packet in capture.sniff_continuously():
    # adjusted output
    localtime = time.asctime(time.localtime(time.time()))

    # get packet content
    protocol = packet.transport_layer  # protocol type
    src_addr = packet.ip.src  # source address
    src_port = packet[protocol].srcport  # source port
    dst_addr = packet.ip.dst  # destination address
    dst_port = packet[protocol].dstport
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=filed_name)

        info = {
            "time":localtime,
            "ip_source":src_addr,
            "ip_dest":dst_addr,
            "protocol":protocol

        }
        print(info)

        csv_writer.writerow(info)
        time.sleep(1)

