#!/usr/bin/python3

#l1=[15,18,22,2,6 ,8]
l1=[4,10,28,9,1,2,17]

def find_unique_pairs(d):
    kk=[]
    for i in d: 
        for k in d: 
            if i!=k: 
                kk.append([i, k])
    print (kk)


    ordered_kk=list(map(lambda x: tuple(sorted(x)), kk))
    print(ordered_kk)
    aa=set(ordered_kk)

    return aa



def main():
    print ("From", l1)
    print(find_unique_pairs(l1))



if __name__=='__main__':
    main()
