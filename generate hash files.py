# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:18:41 2015

@author: correabe
"""

import os
import base64

def num_to_alpha(num):
    num = hex(num)[2:].rstrip("L")

    if len(num) % 2:
        num = "0" + num

    return base64.b64encode(num.decode('hex'))
    
def alpha_to_num(alpha):
    num_bytes = base64.b64decode(alpha)
    return int(num_bytes.encode('hex'), 16)

def get_file_number_from_user_id(user_id):
    user_temp = int(user_id)
    return user_temp % 997
   
def definir_string_user(user_id,lista_artists_N):
    new_line = num_to_alpha(user_id)
    for i in lista_artists_N:
        new_line = new_line+"|"+num_to_alpha(i[0])+":"+str(i[1]) 
    return new_line
   
def insert_line_user_permanent(user_temp,line):
    fo = open("perm/"+str(get_file_number_from_user_id(user_temp))+".txt","a")
    fo.write(linea)
    fo.close()
    
lista =[[1000000,5],[300000,15],[1,15]] 
user= 243  
user_hashed = get_file_number_from_user_id(user)
#print lista[0][1]
    
#linea = definir_string_user(user_id=user,lista_artists_N=lista)    

#insert_line_user_permanent(get_file_number_from_user_id(user),linea)

def get_old_line_user(user):
    fi = open("perm/"+str(get_file_number_from_user_id(user))+".txt","r")
    data = fi.readlines()
    for i in data:
        if alpha_to_num(i.split("|")[0])==user:  
            return i
            
def get_old_artist_count(line):
    user_id = alpha_to_num(line.split("|")[0])
    dictio = {}
    for i in line.split("|")[1:]:
        artist_id,count = i.split(":")        
        artist_id= alpha_to_num(artist_id)        
        dictio[artist_id]=count
    return user_id,dictio

def update_permanent_user_line(user,new_line):
    fi = open("perm/"+str(get_file_number_from_user_id(user))+".txt","r")
    data = fi.readlines()
    position=-1
    for pos,i in enumerate(data):
        if alpha_to_num(i.split("|")[0]) == user:
            position =pos
    
    fi.close()
    if position==-1:
        data.append(new_line)
    else:
        data[position]=new_line
    fi = open("perm/"+str(get_file_number_from_user_id(user))+".txt","w")
    for j in data:
        fi.write(j)
        
        
#lis= get_old_line_user(user)

#u,d= get_old_artist_count(line=lis)   

update_permanent_user_line(243,"U2Ky|D0JA:5|BJPg:15|AQ==:15")





        
#insert_line_user_permanent(get_file_number_from_user_id(1500))
    
