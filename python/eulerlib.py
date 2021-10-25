def is_prime(x):
    if x == 2:
        return True
    else:
        for i in range(2, x):
            if x%i == 0 :
                return False
            return True

# we can use lambda function istead
# is_even = lambda x: x % 2 == 0
def is_even(x):
    return x % 2 == 0
