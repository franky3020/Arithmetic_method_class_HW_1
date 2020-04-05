# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:56:22 2020

@author: frrr
"""

def is_over_BubbleSort(randomList:list)->bool:
    for i in range(len(randomList)):
        for j in range(len(randomList)):
            if randomList[j] > randomList[i]:
                tmp = randomList[j]
                randomList[j] = randomList[i]
                randomList[i] = tmp
    return True

