import argparse
#import common, subnetA, subnetB

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
    parser = argparse.ArgumentParser()
    parser.add_argument("netaddres", help="The network address to be subnetted!")
    parser.add_argument("subnets", help="Number of desired subnets!") #must accomodate the available - for future
    parser.add_argument("-c", "--class", help="IP Class", choices=['A','B','C'])
    net_details = parser.parse_args()

    #num_available_nodes = 2**(DEDICATED_BITS-NUM_OF_BITS_STOLEN) - 2
    DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET = default_value()
    #calling non func step by step as prev called outside functions to solve import issues
    #user details
    NET_ADDRESS, NUM_OF_SUBNETS = get()
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
    print("New subnet mask: %s\n"%(sub_net_mask(DEFAULT_MASK, NUM_OF_BITS_STOLEN, SUBNET_OCTET)))
    print("Number of subnets: %d\n"%(NUM_OF_SUBNETS))
    print("Available node addresses: %d\n"%(num_available_nodes))
    print()






if __name__ == "__main__":
    main()
