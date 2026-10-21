from scapy.all import sniff
from parser import parse_packet

def handle_packet(packet):
    data = parse_packet(packet)

    if data is not None:
        print(data)

def start_capture():
    sniff(prn=handle_packet, store=False)