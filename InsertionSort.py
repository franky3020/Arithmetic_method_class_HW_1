# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:54:08 2020

@author: frrr
"""

def is_over_InsertionSort (randomList:list)->bool:
    for i_insert in range(1, len(randomList)): 
        mainTargetNumber = randomList[i_insert]
        for i_sorted in range(i_insert): 
            sortedNumber = randomList[i_sorted]
            if mainTargetNumber < sortedNumber:  # when find the large number
                del randomList[i_insert] # delete mainTargetNumber
                randomList.insert(i_sorted, mainTargetNumber) # insert to the large number left side
                break
    return True


if __name__ == '__main__': #is for test
    testList=[1,24,21,32,2]
    is_over_InsertionSort(testList)
    print(testList)
