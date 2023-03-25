# This program will calculate the greatest common divisor(gcd) and the lowest common multiple(lcm) of 2 numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

minNumber = min(a,b)
maxNumber = max(a,b)

for i in range(minNumber, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

# a = x * gcd, b = y * gcd, lcm = x * y * gcd
lcm = a * b / gcd

print("The gcd of %d and %d is: %d" %(a, b, gcd))
print("The lcm of %d and %d is: %d" %(a, b, lcm))        