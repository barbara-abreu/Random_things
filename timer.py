#!/usr/bin/python3

#Make timer fot ST

import time
import sys
#TODO- Add progress bar



def exercise(duration, intv, num_rounds):
    print ('{} {:2d} {}\n'.format("Begin exercise with ", num_rounds, "rounds"))
    for i in range(0, num_rounds):
        print ('{} {:2d}'.format("Round", i+1))
        print ("########  10 sec ##########")
        time.sleep(duration)
        if i!=14 and intv>0:
            print ('{} {:1d} {}\n'.format("------ Interval ", intv, "s ------"))
            time.sleep(intv)
        if i==14:
            print ("Done!")
            sys.exit()
            


#Exercises
#lábios

def main():
    exercise(10,3,15)
    
if __name__=='__main__':
    main()
