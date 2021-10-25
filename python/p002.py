#!/bin/env python
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
