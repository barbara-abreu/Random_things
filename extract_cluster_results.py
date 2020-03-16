#!/usr/bin/python3

#Extract cluster results from cluster.log

#Read input
with open('cluster.log') as fp:
    raw=fp.readlines()

dic_clusters={}
a=0
new_cl=[]

#The output will be a dictionary with cluster:[vals,central_s]
for line in raw[12:]:
#For the lines with the cluster number
    if line.split("|")[0] != '    ':
        a=a+1
#After the first line add structures to list
        if a > 1:
            dic_clusters.update({ncluster:[new_cl, central_str]})  

        new_cl=[]
        c=0
        ncluster=int(line.split("|")[0])
        len_cluster=line.split("|")[1]
        central_str=float(line.split("|")[2].split()[0])
        for elem in line.split("|")[3].split():
            new_cl.append(float(elem))
        print ( ncluster, len_cluster, central_str)
#For the lines without the cluster number 
    elif line.split("|")[0] == '    ':
        c=c+1
        for elem in line.split("|")[3].split():
            new_cl.append(float(elem))
     
#Add the final cluster - lazy hack
dic_clusters.update({ncluster:[new_cl, central_str]})



#["ATP" if elem < 5  else "ADP" if elem>=6 and elem <=10 else "Apo" for elem in x ] <- tudo encadeado

def check_state(l_vals):
    return ["ATP" if elem <= 2340000 else  "ADP" if elem>2340000 and elem<=4680000  else "Apo" for elem in l_vals ]

output=open('better_output.log','w')
output.write('{}\t{}\t{}\t{}\t{}\n'.format('CID', 'Size', 'ATP', 'ADP', 'Apo'))

#print (len(dic_clusters)
for cluster in range(1, len(dic_clusters)+1):
    print ("##############################")
    print ("Cluster", cluster)
    print ("Size" ,len(dic_clusters[cluster][0]) )
    print ("ATP", (check_state(dic_clusters[cluster][0]).count("ATP")/len(dic_clusters[cluster][0]))*100)
    print ("ADP", (check_state(dic_clusters[cluster][0]).count("ADP")/len(dic_clusters[cluster][0]))*100)
    print ("Apo", (check_state(dic_clusters[cluster][0]).count("Apo")/len(dic_clusters[cluster][0]))*100)

    output.write('{}\t{}\t{}\t{}\t{}\n'.format(cluster, len(dic_clusters[cluster][0]),(check_state(dic_clusters[cluster][0]).count("ATP")/len(dic_clusters[cluster][0]))*100,(check_state(dic_clusters[cluster][0]).count("ADP")/len(dic_clusters[cluster][0]))*100,(check_state(dic_clusters[cluster][0]).count("Apo")/len(dic_clusters[cluster][0]))*100  ))
