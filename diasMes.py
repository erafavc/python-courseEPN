# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:09:22 2023

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
    
    dys={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    bisiesto=isYearLeap(year)
    
    if bisiesto and month==2:
        return dys[month]+1
    return dys[month]



testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

#print(daysInMonth(1900, 112))
