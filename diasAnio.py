# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:04:37 2023

@author: Administrador
"""

def isYearLeap(yr):
#
# Codigo from LAB Listas y return
#
    if yr%4 == 0 and (yr%100!=0 or yr%400==0):
        return(True)
    else:
        return(False)



def daysInMonth(year, month):
#
# put your new code here
#
    if year<=0 or month<1 or month>12:
        return
    
    dys=[31,28,31,30,31,30,31,31,30,31,30,31]
    bisiesto=isYearLeap(year)
    
    if bisiesto and month==2:
        return dys[month-1]+1
    return dys[month-1]



def dayOfYear(year, month, day):
#
# put your new code here
#
    dom = daysInMonth(year, month)
    
    if year<=0 or month<1 or month>12 or day<1 or day>dom:
        return
    
    doy=0
    
    for i in range(1,month):
        doy += daysInMonth(year, i)
    
    doy += day

    return doy



    
print(dayOfYear(2000, 12, 31))
print(dayOfYear(1901, 12, 31))
print(dayOfYear(2023, 5, 18))
print(dayOfYear(2023, 15, 18))
print(dayOfYear(2023, 5, 33))