import subprocess
import optparse

def getArguments():
    pharser = optparse.OptionParser()
    pharser.add_option("-i", "--iface", dest="iface", help="Interface on which mac change performed")
    pharser.add_option("-m", "--mac", dest="mod_mac", help="New mac")
    return pharser.parse_args()

def changeMac(iface, mod_mac):
    print("[@] Changing MAC to: " + mod_mac + " on " + iface)

    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig", iface, "hw", "ether", mod_mac])
    subprocess.call(["ifconfig", iface, "up"])

(pharserOpt, argum) = getArguments()

changeMac(pharserOpt.iface, pharserOpt.mod_mac)
