# This program is to calculate the CombinatorialNumber C(m,n)
# C(m, n) means the number of ways to get n things out of m same things without caring the sequence to getting them out
# C(m-1, n-1) means the number of ways to divide m same things into n groups

# Factorial function
def fac(num):
    result = 1
    for i in range(1, num + 1, 1):
        result *= i
    return result

# Combinatorial Number function
def C(m, n):
    return fac(m) / (fac(n) * fac(m-n))

if __name__ == '__main__':
    # Only run when this module is excuted directly(then it's name is '__main__')
    m = int(input("Enter the first number: "))
    n = int(input("Enter the second number: "))
    print("C(%d,%d) = %d" %(m,n,C(m,n)))
else:
    # This will excute every time the module is imported
    print("Combinatorial Number import successfully!")