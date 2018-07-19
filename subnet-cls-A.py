print("Subnetting class-A IP addresses\n")
print("================================\n")

#globals
DEFAULT_MASK = ['255','0','0','0'] #1st = 0, 2nd = 1 & so on
BIT_ORDER = [128,64,32,16,8,4,2,1]
DEDICATED_BITS = 24 #for node addresses, Class A

def validate(addr):
    import re
    return True
    """valid = False
    if not valid:
        raise InvalidAdressError('The addres cannot be parsed is that format. :()')
    else:
        return True
"""
def get():
    try:
        net_addr = input("Network address: ").split(sep = '.') #Make a list, separating octets
        if validate(net_addr):
            pass
    except InvalidAdressError:
        print("Provide a valid address: 0.0.0.0")
        get()
    #print("Network address: %s"%(net_addr))
    num_of_subnets = int(input("Number of subnets: "))
    #print("Number  of subnets: %s"%(num_of_subnets))
    return net_addr, num_of_subnets

#user details
NET_ADDRESS, NUM_OF_SUBNETS = get()

#print(NET_ADDRESS)
def bits_stolen():
    global NUM_OF_SUBNETS
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
            if sum == NUM_OF_SUBNETS+1:
                break
    #print("Number of bits stolen: %d"%(num_of_bits_stolen))

    return num_of_bits_stolen

NUM_OF_BITS_STOLEN = bits_stolen()

#Lets find the new Network subnet mask
#helper sum func
def sum(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

def sub_net_mask():
    global NUM_OF_BITS_STOLEN, DEFAULT_MASK
    #We add num_of_bits_stolen higher order bits to get the second octet of subnet mask
    second_octet_mask = sum(BIT_ORDER[:NUM_OF_BITS_STOLEN])
    #print(second_octet_mask)
    sub_network_mask = DEFAULT_MASK
    sub_network_mask[1] = str(second_octet_mask)
    sub_network_mask = '.'.join(sub_network_mask)

    return sub_network_mask

#global for IP ranges
LOWEST_OF_HIGH_ORDER_BITS = min(BIT_ORDER[:NUM_OF_BITS_STOLEN])
#print(LOWEST_OF_HIGH_ORDER_BITS)

def find_ranges():
    #used a helper file because of an error I was yet to identify
    newline = '\n'
    outfile = open("file.txt", 'w')
    global NET_ADDRESS, NUM_OF_SUBNETS, LOWEST_OF_HIGH_ORDER_BITS
    net_addr,num_subnets, octet_increment = NET_ADDRESS, NUM_OF_SUBNETS, LOWEST_OF_HIGH_ORDER_BITS
    for i in range(num_subnets):
        temp = net_addr
        x_temp = int(temp[1])
        x_temp += octet_increment #find starting range ==> uses lowest_of_high_order_bits
        temp[1] = str(x_temp)
        outfile.write(newline)
        outfile.write(str(temp))

    outfile.close()

find_ranges()
def load_and_dump():
    import os
    import os.path
    filename = "file.txt"
    if os.path.isfile(filename):
        pass
    else:
        filename = open('file.txt', 'w+').close() #create it
    ips = []
    file = open(filename, 'r')
    for aline in file.readlines():
        ips.append(aline)

    try:
        file.close()
        if len(ips) > 0:
            file.close()
            os.remove(filename) #Delete the useless file
        else:
            print("Empty list!")
    except Exception as err:
        print(err)

    return ips

range_ips = load_and_dump()
if '\n' in range_ips:
    range_ips.remove('\n')

def clean(range_list):
    """
    clean range IP ready for printing out
    """
    cleaned = []
    for alist in range_list:
        temp = () #startIP, EndIP
        x_temp, y_temp = eval(alist), eval(alist) #x for start, y for end
        x_temp[-1] = '1' #last bit to 1, to make it a node addresses
        y_temp[-3] = str(int(x_temp[-3]) + (LOWEST_OF_HIGH_ORDER_BITS-1)) #the range, for exampe 10.8.0.1 - 10.15.255.254, 16 is left for broadcast/Network
        y_temp[-2], y_temp[-1] = '255', '254' #==> 255.255.255.254
        temp = (x_temp, y_temp)
        #print(temp)
        cleaned.append(temp)

    return cleaned

cleaned_start_end = clean(range_ips)

def print_out():
    global cleaned_start_end
    data = cleaned_start_end
    index = 1
    print("Subnet# \tStart addr    \tEnd addr")
    print("==============================================")
    for atuple in data:
        print("%d. \t%s\t\t%s"%(index,'.'.join(atuple[0]), '.'.join(atuple[1])))
        index+=1

def main():
    num_available_nodes = 2**(DEDICATED_BITS-NUM_OF_BITS_STOLEN) - 2
    print_out()
    print("===============================================")

    print("\n\n")
    print("Network address: %s\n"%('.'.join(NET_ADDRESS)))
    print("Number of subnets: %d\n"%(NUM_OF_SUBNETS))
    print("Available node addresses: %d\n"%(num_available_nodes))
    print()


if __name__ == "__main__":
    main()
