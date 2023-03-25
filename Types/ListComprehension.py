import sys

# List Comprehension

list1 = [x**2 for x in range(0,10)]
print('list1: ', list1)
print(sys.getsizeof(list1))

list2 = [x + y for x in 'abc' for y in '1234']
print(list2)

# Generator

generator = (x**2 for x in range(0,10))
print(generator)
for val in generator:
    print(val)
print(sys.getsizeof(generator))

# Change a function into a generator by using 'yield'
def fibGenerator(n):
    a, b = 0, 1
    # _ means it will not be used in the circle
    for _ in range(n):
        a, b = b, a + b
        yield a

for val in fibGenerator(10):
    print(val)