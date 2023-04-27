# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:28:13 2023

@author: Administrador
"""

def fbn(n):
    if n<0:
        return
    elif n==0:
        return [0]
    elif n==1:
        return [0, 1]
    elif n>=2:
        sf=fbn(n-1)
        vn=sf[n-1]+sf[n-2]
        sf.append(vn)
        return sf
    
print(fbn(9))
