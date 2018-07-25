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


def main(addrs, num_subs, net_class): #intedning to use arg parse
    conflict_values = configure_values(net_class)
