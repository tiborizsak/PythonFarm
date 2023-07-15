import scapy.all as scapey

def szken(ip):
    #scapey.arping(ip)

    arpReq = scapey.ARP(pdst=ip)
    #arpReq.show()

    brdcst = scapey.Ether(dst="ff:ff:ff:ff:ff:ff")
    #brdcst.show()

    arpReqBrdcst = brdcst/arpReq
    #arpReqBrdcst.show()

    #print(arpReq.summary())
    #print(brdcst.summary())

    #scapey.ls(scapey.ARP())
    #scapey.ls(scapey.Ether())

    answered, unanswered = scapey.srp(arpReqBrdcst, timeout=1)
    #print(answered.summary())
    #print(unanswered.summary())
    print(answered[0])

    for e in answered:
        print(e[1].psrc)
        print(e[1].hwsrc)

szken("192.168.0.1/24")