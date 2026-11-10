import parser

all_packets = parser.get_parsed_packets()
all_flows = {}


def parse_flows(packet):

    endpoint_a = (packet['src_ip'], packet['src_port'])
    endpoint_b = (packet['dst_ip'], packet['dst_port'])

    endpoints = tuple(sorted([endpoint_a, endpoint_b]))

    flow_key = (endpoints, packet['protocol'])

    if flow_key not in all_flows:
        all_flows[flow_key] = []

    all_flows[flow_key].append(packet)

        