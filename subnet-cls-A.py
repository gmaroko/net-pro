print("Subnetting class-A IP addresses\n")
print("================================\n")

#globals
DEFAULT_MASK = ['255','0','0','0'] #1st = 0, 2nd = 1 & so on
BIT_ORDER = [128,64,32,16,8,4,2,1]
num_of_bits_stolen = bits_stolen()

#global for IP ranges
lowest_of_high_order_bits = min(BIT_ORDER[:num_of_bits_stolen])
#print(lowest_of_high_order_bits)


def get():
    net_addr = input("Network address: ")
    #print("Network address: %s"%(net_addr))
    num_of_subnets = int(input("Number of subnets: "))
    #print("Number  of subnets: %s"%(num_of_subnets))
    return net_addr, num_of_subnets

def bits_stolen():
    global BIT_ORDER
    num_of_bits_stolen = 0
    sum = 0
    #Lets find the num_of_bits_stolen
    for i in range(len(BIT_ORDER) + 1):
        if i == 0:
            pass
        else:
            pos = -1*i
            sum+=BIT_ORDER[pos]
            num_of_bits_stolen+=1
            if sum == num_of_subnets+1:
                break
    #print("Number of bits stolen: %d"%(num_of_bits_stolen))

    return num_of_bits_stolen


#Lets find the new Network subnet mask
#helper sum func
def sum(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

def sub_net_mask():
    global num_of_bits_stolen
    #We add num_of_bits_stolen higher order bits to get the second octet of subnet mask
    second_octet_mask = sum(BIT_ORDER[:num_of_bits_stolen])
    #print(second_octet_mask)
    sub_network_mask = DEFAULT_MASK
    sub_network_mask[1] = str(second_octet_mask)
    sub_network_mask = '.'.join(sub_network_mask)

    return sub_network_mask

def find_ranges(net_addr, octet_increment):
    range_ips = []
    for i in range(num_of_subnets):
        temp = net_addr
        temp[1] = lowest_of_high_order_bits
        sub_net_addr = temp
        range_ips.append(sub_net_addr)

    return range_ips



def main(_addr, subnets):
    _addr, subnets = get() #input for network address, number of subnets
    print("Subnetted Newtwork mask: %s"%(sub_net_mask()))
    find_ranges()



if __name__ = "__main__":
    main()
