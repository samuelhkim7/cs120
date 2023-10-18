from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    k = math.ceil(math.log(univsize, base))
    n = len(arr)
    vprime = []
    kprime = [0] * n

    for keyval in arr:
        viprime = BC(keyval[0], base, k)
        vprime.append(viprime)

    for j in range (0, k - 1):
        prime = []
        for i in range(0, n - 1):
            kprime[i] = vprime[i][j]
            prime.append([kprime[i], vprime[i]])
        prime = countSort(base, prime)
        vprime = []
        kprime = []
        for i in range (0, n - 1):
            kprime.append(prime[i][0])
            vprime.append(prime[i][1])

    for i in range(0, n - 1):
        sum = 0
        for j in range(0, k - 1):
            sum += vprime[i][j] * pow(base, j)
        orig_tup = arr[i] 
        val = orig_tup[1]
        new_tup = (sum, val)
        arr[i] = new_tup 
    
    return arr

    return [] 
