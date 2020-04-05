# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:34:03 2020

@author: frrr
"""

def is_over_QuickSort (randomList:list)->bool:
    quicksort(randomList, 0, len(randomList) - 1 )
    
def quicksort(input_list:list, left, right):
   
    if left >= right :
        return

    i = left                    
    j = right                    
    target = input_list[left]               

    while i != j:                  
        while input_list[j] > target and i < j:   
            j -= 1
        while input_list[i] <= target and i < j:  
            i += 1
        if i < j:                        
            input_list[i], input_list[j] = input_list[j], input_list[i] 

   
    input_list[left] = input_list[i] 
    input_list[i] = target

    quicksort(input_list, left, i-1)   
    quicksort(input_list, i+1, right)  
        


if __name__ == '__main__': #is for test
    testList=[13,24,21,32,2]
    is_over_QuickSort(testList)
    print(testList)
    