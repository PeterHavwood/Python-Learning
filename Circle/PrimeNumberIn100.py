from math import sqrt

for i in range(2, 101, 1):
    isPrime = True
    for j in range(2, int(sqrt(i)) + 1, 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)