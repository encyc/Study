# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:30:47 2022

@author: Administrator
"""


print('\n'.join([''.join([('lovechenyihui'[(x - y) % 12]if ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 -
      (x * 0.05)**2 * (y * 0.1)**3 <= 0 else ' ')for x in range(-30, 30)])for y in range(15, -15, -1)]))
