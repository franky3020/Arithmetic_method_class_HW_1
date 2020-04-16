# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:45:45 2020

@author: frrr
"""
import time
import random
import csv
from SortArithmeticFactory import sortArithmeticFactory

def count_run_time(sortListFunction:callable(list), randomList:list)->float:
    print("start")
    t1 = time.time()
    sortListFunction(randomList)
    t2 = time.time()
    print("stop")
    print("Run rime: ",t2 - t1)
    return t2 - t1
    
def generateRandomList(listSize:int)->list:
    randomlist = []
    for i in range(0,listSize):
        n = random.randint(1,300000)
        randomlist.append(n)
    return randomlist
    
if __name__ == '__main__':
    
    sortKinds = ["BubbleSort", "SelectionSort", "InsertionSort", "QuickSort"]
    saveSortRunTime = {}
    # init saveSortRunTime
    for sortKind in sortKinds:
        saveSortRunTime[sortKind] = []
    
    
    testArraySizes = [500,1000,1500,2000,2500,3000]
    
    for testArraySize in testArraySizes:
        randomList = generateRandomList(testArraySize)
        
        for sortKind in sortKinds:
            run_time = count_run_time( sortArithmeticFactory(sortKind),  randomList)
            saveSortRunTime[sortKind].append(run_time)
    
    with open('sortRunTime.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(sortKinds)
        for testArraySize in range(len(testArraySizes)):
            
            writer.writerow([saveSortRunTime[sortKinds[0]][testArraySize], \
                            saveSortRunTime[sortKinds[1]][testArraySize], \
                            saveSortRunTime[sortKinds[2]][testArraySize], \
                            saveSortRunTime[sortKinds[3]][testArraySize]])




