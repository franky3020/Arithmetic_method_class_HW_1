# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:47:00 2020

@author: frrr
"""

def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 

    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
        heapify(arr, n, largest) 
        
def heapSort(arr): 
    n = len(arr) 
  
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0) 
        
def is_over_HeapSort(randomList:list)->bool:
    heapSort(randomList)
    return True

if __name__ == '__main__':
    arr = [ 12, 11, 13, 5, 6, 7] 
    is_over_HeapSort(arr) 
    print("test: ", arr)
  
        
        