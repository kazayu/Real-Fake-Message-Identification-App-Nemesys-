# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:14:38 2018

@author: ADMIN
"""

    
import prediction as prd
import sys
import json

#a=input("")
a = ""
for n in range(1,len(sys.argv)):
  a +=" "
  a += str(sys.argv[n])
#user_response=input("")
a=a.strip()
print(json.dumps({"Statement": str(prd.find1(a)), "Possibility": str(prd.find2(a))}))
