from subnetA import get, bits_stolen

#globals
DEFAULT_MASK = ['255','255','0','0'] #1st = 0, 2nd = 1 & so on
BIT_ORDER = [128,64,32,16,8,4,2,1]
DEDICATED_BITS = 16 #for node addresses, Class A

#user details
NET_ADDRESS, NUM_OF_SUBNETS = get()
NUM_OF_BITS_STOLEN = bits_stolen()

#new subnet sub_net_mask
#helper sum func
def sum(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

def sub_net_mask():
    global NUM_OF_BITS_STOLEN, DEFAULT_MASK
    #We add num_of_bits_stolen higher order bits to get the third octet of subnet mask
    thrid_octet_mask = sum(BIT_ORDER[:NUM_OF_BITS_STOLEN])
    #print(second_octet_mask)
    sub_network_mask = DEFAULT_MASK
    sub_network_mask[2] = str(thrid_octet_mask)
    sub_network_mask = '.'.join(sub_network_mask)

    return sub_network_mask

#global for IP ranges
LOWEST_OF_HIGH_ORDER_BITS = min(BIT_ORDER[:NUM_OF_BITS_STOLEN])
#print(LOWEST_OF_HIGH_ORDER_BITS)
