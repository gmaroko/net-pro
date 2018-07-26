import argparse
from common import *
"""
Start of script
Act as a helper to resolve conflict of different values for different classes: eg octets!
"""

def configure_values(a_class):
    clasA, clasB, clsC = {}, {}, {} #store them as dict values

    #class A
    clsA['octet_for_subnet_mask'] = 1 #index == 2nd octet
    clsA['dedicated_bits'] = 24
    clsA['default_mask'] = ['255', '0', '0', '0'] #255.0.0.0

    #class B
    clsB['octet_for_subnet_mask'] = 3 #index == 3rd octet
    clsB['dedicated_bits'] = 16
    clsB['default_mask'] = ['255', '255', '0', '0'] #255.0.0.0

    #class C
    clsC['octet_for_subnet_mask'] = 1 #index == 2nd octet
    clsC['dedicated_bits'] = 8
    clsC['default_mask'] = ['255', '255', '255', '0'] #255.0.0.0

    #avoid return all values to ease processing later
    if a_class == 'A' or 1:
        return clsA
    elif a_class == 'B' or 2:
        return clsB
    elif a_class == 'C' or 3:
        return clsC
    else:
        print("Unknow class!")


def main(): #intending to use argparse
    BIT_ORDER= [128,64,32,16,8,4,2,1]
    parser = argparse.ArgumentParser()
    parser.add_argument("netaddres", help="The network address to be subnetted!")
    parser.add_argument("subnets", type=int ,help="Number of desired subnets!") #must accomodate the available - for future
    parser.add_argument("-c", "--class-ip", choices=['A','B','C', 'a', 'b', 'c'], help="IP Class")

    net_details = parser.parse_args()
    
    if net_details.class_ip == "A" or "a":
        DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET = "255.0.0.0", 24, 1
    elif net_details.class_ip == "B" or "b":
        DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET = "255.255.0.0", 16, 2
    elif net_details.class_ip == "C" or "c":
        DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET = "255.255.255.0", 8, 3

    NET_ADDRESS, NUM_OF_SUBNETS = net_details.netaddres.split(sep="."), net_details.subnets
    #bits stolen
    NUM_OF_BITS_STOLEN = bits_stolen(NUM_OF_SUBNETS)
    #global for IP ranges
    LOWEST_OF_HIGH_ORDER_BITS = min(BIT_ORDER[:NUM_OF_BITS_STOLEN])
    #print(LOWEST_OF_HIGH_ORDER_BITS)
    find_ranges(NET_ADDRESS, NUM_OF_SUBNETS, LOWEST_OF_HIGH_ORDER_BITS)

    range_ips = load_and_dump()
    if '\n' in range_ips:
        range_ips.remove('\n')


    cleaned_start_end = clean(range_ips, LOWEST_OF_HIGH_ORDER_BITS)
    num_available_nodes = 2**(DEDICATED_BITS-NUM_OF_BITS_STOLEN) - 2

    print_out(cleaned_start_end)
    print("===============================================")

    print("\n\n")
    print("Network address: %s\n"%('.'.join(NET_ADDRESS)))
    print("New subnet mask: %s\n"%(sub_net_mask(DEFAULT_MASK.split(sep="."), NUM_OF_BITS_STOLEN, SUBNET_OCTET)))
    print("Number of subnets: %d\n"%(NUM_OF_SUBNETS))
    print("Available node addresses: %d\n"%(num_available_nodes))
    print()






if __name__ == "__main__":
    main()
