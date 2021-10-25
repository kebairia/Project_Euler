#!/bin/env python
from math import *
import time
import numpy as np

# def is_prime(x):
#     if x == 1: 
#         return False
#     elif x == 2: 
#         return True
#     else:
#         for i in range(2, x):
#             if x%i == 0:
#                 return False
#     return True

def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x%i == 0:
                return False
        return True
    return False

def prime_fact(x):
    lst = []
    for i in range(1, x):
        if is_prime(i) and x%i == 0 :
                lst.append(i)
                x = x//i
    lst.append(x)

    return (lst)
    print(lst)
# prime_fact(600851475143)

# start = time.time()
# print("Main result: ",prime_fact(x))
# end = time.time()
# print("time for main is: ", end - start)

start = time.time()
x = 90
res = [i for i in range(1, x) if is_prime(i) and x%i == 0]
res.append(x//np.prod(res))
print("Test result: ",res)
end = time.time()
print("time for test is: ", end - start)
