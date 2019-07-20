from scapy.all import *


def testf(pkt):
    if pkt.haslayer(TCP):
        print("detected tcp packet")


sniff(prn=testf)
