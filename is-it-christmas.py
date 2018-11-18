# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 09:05:23 2018

@author: Nicholas
"""

import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%m-%d')

print('Is it Christmas?')

if st == '12-25':
    print('YES')
else:
    print('NO')
