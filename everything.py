# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:04:24 2015

@author: correabe
"""

import sys
import os
import base64
import re


def get_max_line():

	memory_usage = 0.001
	mem_cons_per_line = 64


	# mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
	# mem_gib = mem_bytes/(1024.**3)
	
	meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
	mem_total_kib = meminfo['MemTotal']  

	max_memory = (mem_total_kib/100)*memory_usage
	max_lines = (max_memory*1024)/mem_cons_per_line

	return max_lines


def read_file(file_name):

	max_line = 5
	s_line = 1
	e_line = max_line


	with open(file_name) as fi:

		tmp_user_info = {}

		for n,line in enumerate(fi):
			n+=1

			print(n)

			if n > e_line:
				s_line = n
				e_line = s_line + (max_line-1)

				for user_id in tmp_user_info:
					update_artist_count(user_id, tmp_user_info[user_id])

				print('*** end of a sequence ***')

				tmp_user_info = {}


			if n >= s_line and n <= e_line:

				line=line.strip()

				if line:

					user_id,country_code,artist_id,track_id = line.split('|')

					if user_id not in tmp_user_info:
						tmp_user_info[user_id] = {}

					if artist_id not in tmp_user_info[user_id]:
						tmp_user_info[user_id][artist_id]=0

					tmp_user_info[user_id][artist_id]+=1

def update_artist_count(user_id, user_info):

    old_line = get_old_line_user(user_id)
    
    if old_line is not None:
        user_id, old_user_info = get_old_artist_count(old_line)
        for artist_id in user_info:
            if artist_id in old_user_info:
                user_info[artist_id] = user_info[artist_id] + old_user_info[artist_id]


    modify_line(user_id, user_info)


def modify_line(user_id, user_info):

	new_line = user_id

	for artist_id in user_info:
		new_line = new_line+"|"+num_to_alpha(artist_id)+":"+str(user_info[artist_id])

	return new_line
 
def get_old_artist_count(line):
    if line is not None:
        user_id = alpha_to_num(line.split("|")[0])
        dictio = {}
        for i in line.split("|")[1:]:
            artist_id,count = i.split(":")        
            artist_id= alpha_to_num(artist_id)        
            dictio[artist_id]=count
            return user_id, dictio
    else:
        return None,None

def alpha_to_num(alpha):
    num_bytes = base64.b64decode(alpha)
    return int(num_bytes.encode('hex'), 16)

def get_file_number_from_user_id(user_id):

	user_temp = int(user_id)
	return user_temp % 997
def num_to_alpha(num):

	num = hex(num)[2:].rstrip("L")

	if len(num) % 2:
		num = "0" + num
	return base64.b64encode(num.decode('hex'))
 
def get_old_line_user(user_id):
    if os.path.exists("perm/"+str(get_file_number_from_user_id(user_id))+".txt"):
        fi = open("perm/"+str(get_file_number_from_user_id(user_id))+".txt","r")
        data = fi.readlines()
        for pos,i in enumerate(data):
            if alpha_to_num(i.split("|")[0])==user_id:  
                return i
    else:
        return None
            
read_file("perm/dayfile.txt")
	