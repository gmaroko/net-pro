print("Subnetting class-A IP addresses\n")
print("================================\n")

DEFAULT_MASK = ['255','0','0','0'] #1st = 0, 2nd = 1 & so on
BIT_ORDER = [128,64,32,16,8,4,2,1]
net_addr = input("Network address: ")
print("Network address: %s"%(net_addr))
num_of_subnets = int(input("Number of subnets: "))
print("Number  of subnets: %s"%(num_of_subnets))

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
print("Number of bits stolen: %d"%(num_of_bits_stolen))

#Lets find the new Network subnet mask
#We add num_of_bits_stolen higher order bits to get the second octet of subnet mask
def sum(list):
    sum = 0
    for i in list:
        sum+=i
    return sum
second_octet_mask = sum(BIT_ORDER[:num_of_bits_stolen])
print(second_octet_mask)


sub_network_mask = DEFAULT_MASK
sub_network_mask[1] = str(second_octet_mask)
sub_network_mask = '.'.join(sub_network_mask)

#IP ranges
lowest_of_high_order_bits = min(BIT_ORDER[:num_of_bits_stolen])
print(lowest_of_high_order_bits)

def find_ranges(net_addr, lowest_of_high_order_bits):
    range_ips = []
    for i in range(num_of_subnets):
        temp = net_addr
        temp[1] = lowest_of_high_order_bits
        sub_net_addr = temp
        range_ips.append(sub_net_addr)

    return range_ips
