import subprocess
import optparse

def changeMac(iface, mod_mac):
    print("[@] Changing MAC to: " + mod_mac + " on " + iface)

    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig", iface, "hw", "ether", mod_mac])
    subprocess.call(["ifconfig", iface, "up"])

pharser = optparse.OptionParser()

pharser.add_option("-i", "--iface", dest="iface", help="Interface on which mac change performed")
pharser.add_option("-m", "--mac", dest="mod_mac", help="New mac")

(pharserOpt, argum) = pharser.parse_args()

changeMac(pharserOpt.iface, pharserOpt.mod_mac)
