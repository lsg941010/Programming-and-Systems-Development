# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:08:45 2019

@author: 2443170L
"""

import numpy as np
import os 
'This is not nesseary'
x=np.arange(9).reshape(3,3)
print("the array")
print(x)
header='col1 col2 col3 col4'
np.savetxt('temp.txt',x,fmt="%d",header=header)
print("after loading content of the text file")
result=np.loadtxt('temp.txt')
print(result)