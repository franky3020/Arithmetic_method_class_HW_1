# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:33:44 2020

@author: frrr
"""

import unittest
from BubbleSort import is_over_BubbleSort 
from SelectionSort import is_over_SelectionSort
from InsertionSort import is_over_InsertionSort
from QuickSort import is_over_QuickSort
from HeapSort import is_over_HeapSort

class TestSort(unittest.TestCase):
    
    def test_BubbleSort(self):
        testList = [2,50,4,20,2,11,3,5]
        is_over_BubbleSort(testList)
        self.assertEqual(testList, [2, 2, 3, 4, 5, 11, 20, 50])
        
    def test_SelectionSort(self):
        testList = [2,50,4,20,2,11,3,5]
        is_over_SelectionSort(testList)
        self.assertEqual(testList, [2, 2, 3, 4, 5, 11, 20, 50])
        
    def test_InsertionSort(self):
        testList = [2,50,4,20,2,11,3,5]
        is_over_SelectionSort(testList)
        self.assertEqual(testList, [2, 2, 3, 4, 5, 11, 20, 50])
        
    def test_QuickSort(self):
        testList = [2,50,4,20,2,11,3,5]
        is_over_QuickSort(testList)
        self.assertEqual(testList, [2, 2, 3, 4, 5, 11, 20, 50])
        
    def test_HeapSort(self):
        testList = [2,50,4,20,2,11,3,5]
        is_over_HeapSort(testList)
        self.assertEqual(testList, [2, 2, 3, 4, 5, 11, 20, 50])
 

if __name__ == '__main__':
    unittest.main()


