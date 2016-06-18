# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:58:45 2015

@author: correabe
"""

import base64

def num_to_alpha(num):
    num = hex(num)[2:].rstrip("L")

    if len(num) % 2:
        num = "0" + num

    return base64.b64encode(num.decode('hex'))
    

def alpha_to_num(alpha):
    num_bytes = base64.b64decode(alpha)
    return int(num_bytes.encode('hex'), 16)

print num_to_alpha(1052)
print alpha_to_num("E7A=")




