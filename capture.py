
from scapy.all import sniff
from parser import parse_packet

packets_captured = 0
packets_parsed = 0


def handle_packet(packet):
    global packets_captured, packets_parsed

    packets_captured += 1

    data = parse_packet(packet)

    if data is not None:
        packets_parsed += 1


def start_capture(interface=None, packet_filter=None):

    try:
        sniff(
            iface=interface,
            filter=packet_filter,
            prn=handle_packet,
            store=False
        )

    except Exception as error:
        pass


def stop_capture():
    pass
