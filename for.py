#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:06:25 2020

@author: andrew
"""
import numpy as np
import matplotlib.pyplot as plt

oper_list = []
for i in range(10):
    operatee = i+1
    operator = operatee**2
    print(' {}^2 = {}'.format(operatee, operator))
    
    
    'can also create and store values in a list (has to be defined \
        first (line 11)'
    oper_list.append([operatee**2, operatee+5, 4*np.sin(operatee)])


'we print to see what type of list has been generated..'
print('\nthis is the original list:')
print(oper_list)
'this converts the list to an array'
oper_list = np.array(oper_list)
'transposing the array allows us to generate a single vector for each \
    operation as displayed in line 20'
trp_list = oper_list.transpose()
'print again to see what I mean'
print('\nthis is the transposed list:')
print(trp_list)

'plot it'
plt.plot(oper_list)