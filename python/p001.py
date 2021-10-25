#!/bin/env python
def is_mul3(x):
    return x%3 == 0

def is_mul5(x):
    return x%5 == 0
sum = 0
for i in range(1, 1000):
    if is_mul3(i) or is_mul5(i):
        sum += i
print("The result is: ", sum)
