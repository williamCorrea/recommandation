# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:21:32 2015

@author: correabe
"""

import numpy as np
import sys


fo=open("perm/dayfile.txt","w")
for i in range(0,5):
    user = int((16000000)*np.random.random())
    artist = int(3500000*np.random.random())
    track = int(35000000*np.random.random())
    line = str(user)+'|FR|'+str(artist)+'|'+str(track)
    fo.write(line+"\n")

fo.close()
print "done"