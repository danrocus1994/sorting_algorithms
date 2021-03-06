#!/usr/bin/python3
import math

def sort(array, radix=10):
    if len(array) == 0:
        return array
    minvalue = array[0]
    maxvalue = array[0]
    for i in range(1, len(array)):
        if array[i] < minvalue:
            minvalue = array[i]
        elif array[i] > maxvalue:
            maxvalue = array[i]

    exponent = 1
    while (maxvalue-minvalue) / exponent >=1:
        array = countingSortByDigit(array, radix, exponent, minvalue)
        print(array)
        exponent *= radix

    return array

def countingSortByDigit(array, radix, exponent, minvalue):
    bucketIndex = -1
    buckets = [0] * radix
    output = [None] * len(array)
    for i in range(0, len(array)):
        bucketIndex = math.floor(((array[i]) / exponent) % radix)
        #print("pos: ", i, "b_index: ", bucketIndex, "val: ", array[i])
        #print(bucketIndex, " ", end="")
        if bucketIndex < 1:
            bucketIndex = bucketIndex * 10
        buckets[bucketIndex] += 1
    print()
    print("buckets", buckets)
    for i in range(1, radix):
        buckets[i] += buckets[i - 1]
        #print(buckets[i], " ", end="")
    #print()
    #print("buckets", buckets)

    for i in range(len(array) - 1, -1, -1):
        bucketIndex = math.floor(((array[i]) / exponent) % radix)
        if bucketIndex < 1:
            bucketIndex = bucketIndex * 10
        buckets[bucketIndex] -= 1
        print(buckets[bucketIndex]," out: ", array[i])
        output[buckets[bucketIndex]] = array[i]

    return output
