#!/usr/bin/python3

#Random phone number generator

import random

def generate_number():
    network=['1','2','3','6']
    ndx_net=random.randrange(0,len(network))
    return '9'+str(network[ndx_net])+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

    
for i in range(0,1000):   
    print (generate_number())



