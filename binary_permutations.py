#!/usr/bin/python3

#Binary permutation

def permutation(num_bits):
    if num_bits >0:
        binary[num_bits-1]=0
        permutation(num_bits-1)
        binary[num_bits-1]=1
        permutation(num_bits-1)
    else:
        print(binary)

binary=[0,0,0,0]
print (permutation(len(binary)))

    
