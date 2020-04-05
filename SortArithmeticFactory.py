# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:04:27 2020

@author: frrr
"""


def sortArithmeticFactory(sortName:str)->callable:
    if sortName == "BubbleSort":
        from BubbleSort import is_over_BubbleSort 
        return is_over_BubbleSort
    elif sortName == "SelectionSort":
        from SelectionSort import is_over_SelectionSort
        return is_over_SelectionSort
    