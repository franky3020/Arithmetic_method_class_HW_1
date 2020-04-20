# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:45:45 2020

@author: frrr
"""
import time
import random
import csv
from SortArithmeticFactory import sortArithmeticFactory

def count_run_time(sortListFunction, randomList:list)->float:
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
        n = random.randint(1,3000)
        randomlist.append(n)
    return randomlist
    
if __name__ == '__main__':
    
    sortKinds = ["BubbleSort", "SelectionSort", "InsertionSort", "QuickSort", "HeapSort"]
  
    saveSortRunTime = {}
    # init saveSortRunTime
    for sortKind in sortKinds:
        saveSortRunTime[sortKind] = []
    
    
    testArraySizes = [50000, 100000, 150000, 200000, 250000, 300000]
    
    for testArraySize in testArraySizes:
        randomList = generateRandomList(testArraySize)
        
        for sortKind in sortKinds:
            randomList_copy = randomList.copy()
            run_time = count_run_time( sortArithmeticFactory(sortKind),  randomList_copy)
            saveSortRunTime[sortKind].append(run_time)
    
    with open('sortRunTime.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(sortKinds)
        for testArraySize in range(len(testArraySizes)):
            
            out_csv_save = []
            for i in range(len(sortKinds)):
                out_csv_save.append(saveSortRunTime[sortKinds[i]][testArraySize])
            writer.writerow(out_csv_save)




