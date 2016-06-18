# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:08:46 2015

@author: correabe
"""

import sys
import os
import base64
import re





def alpha_to_num(alpha):
    num_bytes = base64.b64decode(alpha)
    return int(num_bytes.encode('hex'), 16)

   
def insert_line_user_permanent(user_temp,line):


	fo = open("perm/"+str(user_temp)+".txt","a")
	fo.write(line)
	fo.close()



def num_to_alpha(num):

	num = int(num)

	num = hex(num)[2:].rstrip("L")

	if len(num) % 2:
		num = "0" + num
	return base64.b64encode(num.decode('hex'))


def get_file_number_from_user_id(user_id):

	user_temp = int(user_id)
	return user_temp % 997


def modify_line(user_id, user_info):

	new_line = user_id

	for artist_id in user_info:
		new_line = new_line+"|"+num_to_alpha(artist_id)+":"+str(user_info[artist_id])


	return new_line





def get_old_line_user(user_id):
    fi = open("perm/"+str(get_file_number_from_user_id(user_id))+".txt","r")
    data = fi.readlines()
    for pos,i in enumerate(data):
        if alpha_to_num(i.split("|")[0])==user_id:  
            return i



def get_old_line_user(user_id):

	if os.path.exists("perm/"+str(get_file_number_from_user_id(user_id))+".txt"):

		fi = open("perm/"+str(get_file_number_from_user_id(user_id))+".txt","r")

		data = fi.readlines()

		for pos,i in enumerate(data):

			if alpha_to_num(i.split("|")[0])==user_id:
				return i
	else:

		return None




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







def update_artist_count(user_id, user_info):

    print user_id    
    print(user_info)
    
    old_line = get_old_line_user(user_id)
    print old_line

	# if not old_line:
	# 	fo = open("perm/"+str(get_file_number_from_user_id(user_temp))+".txt","a")
	# 	insert_line_user_permanent(user_id, )

    _user_id, old_user_info = get_old_artist_count(old_line)

    for artist_id in user_info:
        if old_user_info:
            if artist_id in old_user_info:
                user_info[artist_id] = user_info[artist_id] + old_user_info[artist_id]


    new_line = modify_line(user_id, user_info)
    insert_line_user_permanent(user_id, new_line)



def read_file(file_name):

	max_line = 9 #get_max_line()
	s_line = 1
	e_line = max_line


	with open(file_name) as fi:

		tmp_user_info = {}

		for n,line in enumerate(fi):
			n+=1

			if n >= e_line:

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





		


def replace(filePath, text, subs, flags=0):
    with open( filePath, "r+" ) as file:
        fileContents = file.read()
        textPattern = re.compile( re.escape( text ), flags )
        fileContents = textPattern.sub( subs, fileContents )
        file.seek( 0 )
        file.truncate()
        file.write( fileContents )


def update_file(user_id, user_info):

	for artist_id in user_info:
		listen_count = user_info[artist_id]

		print (user_id, artist_id, listen_count)

		# define_string_user(user_id, lista_artists_N)




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





def main():

	# lista =[[1000000,5],[300000,15],[1,15]]
	# user= 5464754
	# print define_string_user(user_id=user,lista_artists_N=lista) 



	file_name = "perm/dayfile.txt"
	# replace(file_name, '10198246|FR|1384662|31108118', '10198245|FR|1384662|31108118')

	read_file(file_name)


if __name__ == '__main__':
	main()