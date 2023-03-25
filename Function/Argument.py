# There are some common things in Python and C#, like the defult argument and the way to pass arguments regardless of their order
# But because of the dynamic type in Python, it's easy to ues function with different types of arguments without Overrides

def add(a = 0, b = 0):  # The defult value of a, b is 0
    return a + b

def addWithAnyArgumentNumber(*avg):  # '*' means avg is a variable argument, it cant have a defult value
    result = 0
    for i in avg:
        result += i
    return result

print(add())
print(add(1))
print(add(1, 2))
print(add(b = 1, a = 2))
print(add(1.2, 4.5))

print(addWithAnyArgumentNumber(0))
print(addWithAnyArgumentNumber(1.2, 3.4, 5.3))