# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:54:27 2023

@author: Administrador
"""

def readint(prompt, min, max):
    while True:
        try:
            resp=int(input(prompt))
        except:
            print("¡Error en el ingreso!")
        else:
            if resp<min or resp>max:
                print("Error: el valor no está en el rango permitido (%d..%d)" % (min,max))
            else:
                return resp
            
""""""        
    
mn=-8
mx=20
txt="Ingrese un número entre "+str(mn)+" hasta "+str(mx)+" :  "

v = readint(txt, mn, mx)

print("The number is:", v)
