filters = {
    "TCP": "tcp",
    "UDP": "udp",
    "DNS": "dns",
    "ARP": "arp",
    "ICMP": "icmp"
}

for name in filters:
    print(name, "filter =", filters[name])

print("TCP handshake = SYN -> SYN-ACK -> ACK")
