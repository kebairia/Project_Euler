#!/bin/env python
is_mul3 = lambda x: x%3 == 0
is_mul5 = lambda x: x%5 == 0
print("Thre result is: ", sum([x for x in range(1,1000) if is_mul3(x) or is_mul5(x)]))

is_even = lambda x: x % 2 == 0
def fib(limit):
    lst = []
    x, y, ans = 0, 1, 1
    while x <= limit:
        lst.append(ans)
        ans += y
        x, y = y, x + y
    return lst
print("The result is: ", sum([x for x in fib(4000000) if is_even(x)]))
