def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n != 0

def primes():
    yield 2
    iter = _odd_iter()
    while True:
        n = next(iter)
        yield n
        # Everytime you call filter, you will add a restriction on the generator
        # And when you call the generator for next value, it will check if the value suit for all restrictions before
        iter = filter(_not_divisible(n), iter)

for n in primes():
    if n < 100:
        print(n)
    else:
        break