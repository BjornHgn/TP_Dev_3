import psutil
import netaddr

def get_ip():
    scan = psutil.net_if_addrs()
    wifi = (scan["Wi-Fi"])
    mask = netaddr.IPAddress(wifi[1].netmask).netmask_bits()
    addresses = pow(2,(32-mask))
    print(wifi[1].address + "/" +  str(mask))
    print(str(addresses) + " adresses")

get_ip()