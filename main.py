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
    inputs = parser.parse_args()

    print(inputs)





if __name__ == "__main__":
    main()
