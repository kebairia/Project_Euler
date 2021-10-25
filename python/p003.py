#!/bin/env python
from math import *

def is_prime(x):
    if x == 1 :
        return False
    if x == 2:
        return True
    else:
        for i in range(2, x):
            if x%i == 0 :
                return False
            return True
def prime_fact(x):
    lst = []
    for i in range(1, x):
        if is_prime(i) and x%i == 0 :
                lst.append(i)
                x = x/i
    lst.append(x)

    print(max(lst))
    print(lst)
# prime_fact(600851475143)
prime_fact(60085147)
#
