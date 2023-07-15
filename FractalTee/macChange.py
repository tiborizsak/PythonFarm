import subprocess
import optparse
import re

def getMac():
    ifconfig_result = str(subprocess.check_output(["ifconfig", pharserOpt.iface]))
    result_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    return(result_mac.group(0))

def getArguments():
    # The script is expecting the user to enter arguments as cmd parameters
    pharser = optparse.OptionParser()
    #pharser.add_option("-h", "--help", help="The script is meant to change the MAC address of the machine. The app expects the interface and the new MAC as a command parameter.")
    pharser.add_option("-i", "--iface", dest="iface", help="Interface on which mac change performed")
    pharser.add_option("-m", "--mac", dest="mod_mac", help="New mac")
    return pharser.parse_args()

def changeMac(iface, mod_mac):
    print("[@] Recent MAC: " + getMac())
    print("[@] Changing MAC to: " + mod_mac + " on " + iface)

    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig", iface, "hw", "ether", mod_mac])
    subprocess.call(["ifconfig", iface, "up"])

    if mod_mac == getMac():
        print("[@] MAC change successful")
    else:
        print("[@] Something went wrong during MAC change")

(pharserOpt, argum) = getArguments()

changeMac(pharserOpt.iface, pharserOpt.mod_mac)

getMac()