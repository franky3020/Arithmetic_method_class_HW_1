# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:04:27 2020

@author: frrr
"""
from BubbleSort import is_over_BubbleSort
from SelectionSort import is_over_SelectionSort 
from InsertionSort import is_over_InsertionSort
from QuickSort import is_over_QuickSort
from HeapSort import is_over_HeapSort

def sortArithmeticFactory(sortName:str)->callable:
    if sortName == "BubbleSort":
        return is_over_BubbleSort
    elif sortName == "SelectionSort":
        return is_over_SelectionSort
    elif sortName == "InsertionSort":
        return is_over_InsertionSort
    elif sortName == "QuickSort":
        return is_over_QuickSort
    elif sortName == "HeapSort":
        return is_over_HeapSort
    