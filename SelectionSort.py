# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:01:25 2020

@author: frrr
"""

def is_over_SelectionSort(randomList:list)->bool:
    for i in range(len(randomList) - 1): # beacuse the last one can ignore
        
        min = i   
        for j in range(i, len(randomList)): 
            if randomList[j] < randomList[min]: 
                min = j 
                
        if i != min:
            randomList[min], randomList[i] = randomList[i], randomList[min] 

    return True

