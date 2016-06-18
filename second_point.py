# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 19:14:14 2015

@author: correabe
"""
import numpy as np
import scipy.spatial as spd


clusters = {}

cluster_0=[]
cluster_1=[]
cluster_2=[]
cluster_3=[]
cluster_4=[]
cluster_5=[]
cluster_6=[]
cluster_7=[]
cluster_8=[]
cluster_9=[]


def generate_users_and_clusters(taille):
    

    for i in range (0,taille):
        value  = ((10)*np.random.random())
        clusters[i] = int(value)



    for i in clusters:
        for j in clusters:
            cl = clusters[i]
            if i<j :
                if cl==clusters[j]:
                    stri_cl = "cluster_"+str(cl)
                    t=globals()[stri_cl]              
                    temp=[i,j,np.random.random()]
                    t.append(temp)
    print cluster_0
    return clusters,cluster_0,cluster_1,cluster_2,cluster_3,cluster_4,cluster_5,cluster_6,cluster_7,cluster_8,cluster_9
              



def insert_value_list(new_user,val,list_values,list_users):
    #print lista
    max_value = max(list_values)
    if val<max_value:
        max_index = list_values.index(max_value)
        list_values[max_index]=val
        list_users[max_index]= new_user
    return list_values,list_users

def getSimilarUsers(user):
    #print clusters
    cl = clusters[user]
    values=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    users=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]    

    stri_cl = "cluster_"+str(cl)
   
    t=globals()[stri_cl]     
    for i in t:
        #print i
        if i[0]==user or i[1]==user:
            if i[0]==user:
                values,users=insert_value_list(i[1],i[2],values,users)
            else:
                values,users=insert_value_list(i[0],i[2],values,users)    
    return users,values


clusters,cluster_0,cluster_1,cluster_2,cluster_3,cluster_4,cluster_5,cluster_6,cluster_7,cluster_8,cluster_9=generate_users_and_clusters(100)
users,values=getSimilarUsers(16)

#print cluster_0

print "20 most similar users"
print users
print "distances from the 20 most similar users to our user"
print values

    

    
    
#==============================================================================
# the_bests=[0.2,0.5,0.3,0.9,1,1]
# users = [15,2,5,65,32,4]
# 
# a,b=insert_value_list(54,0.4,the_bests,users)
# 
# print a
# print b
# 
# a,b=insert_value_list(98,0.1,the_bests,users)
#==============================================================================

