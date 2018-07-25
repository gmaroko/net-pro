from common import *
#globals
def default_value():
    setup = configure_values('A') #a dictionary of default values
    DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET= setup['default_mask'], setup['dedicated_bits'], setup['octet_for_subnet_mask']
    return DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET

def main():
    DEFAULT_MASK, DEDICATED_BITS, SUBNET_OCTET = default_value()
    #num_available_nodes = 2**(DEDICATED_BITS-NUM_OF_BITS_STOLEN) - 2

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
