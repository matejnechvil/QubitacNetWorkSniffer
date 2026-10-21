from scapy.all import IP, TCP, UDP

def parse_packet(packet):

    if IP not in packet:
        return None

    data = {
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "protocol": "OTHER",
        "src_port": None,
        "dst_port": None,
        "size": len(packet)
    }

    if TCP in packet:
        data["protocol"] = "TCP"
        data["src_port"] = packet[TCP].sport
        data["dst_port"] = packet[TCP].dport

    elif UDP in packet:
        data["protocol"] = "UDP"
        data["src_port"] = packet[UDP].sport
        data["dst_port"] = packet[UDP].dport

    return data