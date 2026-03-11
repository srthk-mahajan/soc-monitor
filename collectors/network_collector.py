from scapy.all import sniff, TCP, IP
from detection.network_rules import process_packet


def packet_callback(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags

        process_packet(src_ip, dst_port, flags)


def start_network_collector():

    print("[+] Network telemetry monitoring started")

    sniff(
        iface=["lo","wlp2s0"],
        filter="tcp",
        prn=packet_callback,
        store=False
    )