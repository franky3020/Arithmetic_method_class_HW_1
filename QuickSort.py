# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:34:03 2020

@author: frrr
"""

def is_over_QuickSort (randomList:list)->bool:
    quicksort(randomList, 0, len(randomList) - 1 )
    
    
def quicksort(input_list:list, left, right):
    
    subRange = []
    
    if left < right :
        subRange.append(right)
        subRange.append(left)
        
        while(len(subRange) > 0):
            in_Range_left_i = subRange.pop()
            in_Range_right_i = subRange.pop()
            mid_index = partition(input_list, in_Range_left_i, in_Range_right_i)
            if(mid_index > in_Range_left_i + 1 ):
                subRange.append( mid_index - 1 ) # push right index
                subRange.append( in_Range_left_i ) # push left index
            
            if(mid_index < in_Range_right_i - 1):
                subRange.append( in_Range_right_i ) # push right index
                subRange.append( mid_index + 1 ) # push left index
        
        
def partition(input_list:list, left, right):
    target = input_list[left];
    while (left < right):
        while (left < right and target <= input_list[right]):
            right = right - 1
        input_list[left] = input_list[right];
        
        while (left < right and target >= input_list[left]):
            left = left + 1
        input_list[right] = input_list[left];
    
    input_list[left] = target;
    return left;


if __name__ == '__main__': #is for test
    testList=[13,24,21,32,2]
    is_over_QuickSort(testList)
    print(testList)
    