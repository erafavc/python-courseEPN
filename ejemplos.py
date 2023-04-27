# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""cls para línea de comandos"""

5+3**2
print(5**3)
print("holita")

x=3.3756563
i=5
s="TXT"
print(type(x))
print("valor %f y %d con %s" % (x, i, s))
print("otra forma {:.2f} y {:d} con {:s}".format(x,i,s))
print("\n"*2)

"""lista es dinamica"""
lista=[3,1.8,'hola',False]
print("Ej lista",lista)
lista[3]=36
del lista[2]
print("Lista cambia", lista)

"""tupla es como una constante no cambia valores"""
tupla=(4,2.8,"bye",True)
print("Ej tupla",tupla)
"""esto no funciona
tupla[2]=4.4
del tupla[2]
"""
print("\n")

"""diccionario"""
dicc={34:"edad",
      True:3.1416,
      "edad":28,
      2.88:False,
      "edad":[28,50]}
print("Ej diccionario: ",dicc)
print("elemento 34: ", dicc[34])
print("Elemento anidado", dicc["edad"][0])
print("\n")


"""ingreso de datos"""
nombre=input("ingrese el nombre: ")
dato=int(input("ingrese un entero: "))
decimal=float(input("Ingrese un numero real: "))
print("Su nombre es",nombre,". Entero",dato,". Real",decimal)
type(nombre)
type(dato)
print("\n")

"""Condicional"""
edad=int(input("Ingrese su edad: "))
if edad==28:
    edad=50
    print("Su edad es 28")
elif edad<28:
    print("su edad es menos de 28")
else:
    print("su edad es mas de 28")
print("se conoce el fin por el identado")
print("\n")

"""ciclo for"""
o=[]
texto="CEC EPN curso python ESS"
for i in texto:
    if "o" in i:
        o.append(i)
    print(i,end=".")
print(o)
print("\n")

lista=["a","b","c","d"]
for elemt in lista:
    print(elemt,end="*")
    if elemt=="c":
        print("<-->",end="")
print("\n")
    

"""ciclo while"""
fin=int(input("Ingrese el número final: "))
contd=1
while contd<=fin:
    print(contd)
    contd+=1
    
while True:
    x=input("number (q or x para terminar): ")
    if x=='q' or x=='x':
        break 
    x=int(x)  
    print(2**x)
print("\n")


"""funciones"""
def msj():
    x=print("Cual es su nombre: ")
    print("Cual es su edad:  ")
print("usted escribio") """x no se pasa"""

def crealst(n):
    lst=[]
    for item in range(1,n+1,1):
        lst.append(item)
    return lst
n=int(input("Ingrese No. "))
print(crealst(n))
print("\n")
