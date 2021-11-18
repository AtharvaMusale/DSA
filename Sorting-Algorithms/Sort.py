# -*- coding: utf-8 -*-
"""Sorting Algorithms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zs3AsvgNWFxGBJqi0oMr7NuekWVzAlCx
"""

import numpy as np
import time

"""<pre>
Stable Sorting Algorithms - Bubble Sort, Merge Sort, Insertion Sort

Unstable Sorting Algorithm - Selection Sort, Quick Sort, Heap Sort
</pre>
"""

"""
Bubble Sort - Stable Algorithm, Inplace Algorithm
"""
def Swap_Var(a,b):
  a,b = b,a
  return a,b

def BubbleSort(arr,n):
  swap = False
  for i in range(n-1):
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = Swap_Var(arr[j],arr[j+1])
        Swap = True
    if Swap == False:
      break
  return arr

def test():

  arr = np.random.randint(1,10,6)
  print("Original array is: {}".format(arr))
  begin = time.time()
  print("Sorted Array Using Bubble Sort is: {}".format(BubbleSort(arr,len(arr))))
  end = time.time()
  print('Time taken to execute Bubble Sort is: {}'.format(end-begin))
test()

"""
Selection Sort -  Not a stable algorithm, In Place
Very efficient in memory writes but not as efficient as Cycle Sort
"""
def Swap(a,b):
  return b,a


def SelectionSort(arr):
  n = len(arr)
  for i in range(n-1):
    min_ind = i
    for j in range(i+1,n):
      if arr[j]<arr[min_ind]:
        arr[j],arr[min_ind] = Swap(arr[j],arr[min_ind])
  
  return arr

def test():
  arr = np.random.randint(1,10,6)
  print("Original array is: {}".format(arr))
  begin = time.time()
  print("Sorted Array Using Bubble Sort is: {}".format(SelectionSort(arr)))
  end = time.time()
  print('Time taken to execute Bubble Sort is: {}'.format(end-begin))
test()

"""
Insertion Sort - Stable, In Place Algorithm
Used in practically small arrays in TimSort
O(n^2) in worst case and O(n) in best case
"""
def InsertionSort(arr):
  n = len(arr)
  for i in range(1,n):
    j=i-1
    key = arr[i]
    while j>=0 and arr[j]>key:
      arr[j+1] = arr[j]
      j-=1  
    arr[j+1] = key
    
  return arr


def test():

  arr = np.random.randint(1,10,6)
  print("Original array is: {}".format(arr))
  begin = time.time()
  print("Sorted Array Using Insertion Sort is: {}".format(InsertionSort(arr)))
  end = time.time()
  print('Time taken to execute Insertion Sort is: {}'.format(end-begin))
test()

"""<pre>
# **Merge Sort**
* Divide and Conquer algorithm
* Stable Algorithm
* Theta(n logn) time and O(n) space complexity
* Well suited for linked list  works in O(1)
* Used in external sorting and in TimSort
* In general for arrays QuickSort outperforms MergeSort
</p>
"""

"""
Merging the two sorted arrays
"""
def MergeTwoSortedLists(arr1, arr2):
  result = []
  m = len(arr1)
  n = len(arr2)
  i,j = 0,0
  while i<m and j<n:
    if arr1[i]<=arr2[j]:
      print(arr1[i])
      i+=1
  
    else:
      print(arr2[j])
      j+=1

  while i<m:
    print(arr1[i])
    i+=1
  
  while j<n:
    print(arr2[j])
    j+=1


def test():
  arr1 = sorted(np.random.randint(1,10,6))
  print("Original array1 is: {}".format(arr1))
  arr2 = sorted(np.random.randint(1,10,6))
  print("Original array1 is: {}".format(arr2))
  begin = time.time()
  print("Running the MergeTwoSortedLists{}".format(MergeTwoSortedLists(arr1,arr2)))
  end = time.time()
  print('Time taken to execute Insertion Sort is: {}'.format(end-begin))
test()

"""
Merge Function for Merge Sort
"""