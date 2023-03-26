import sys

# List Comprehension

list1 = [x**2 for x in range(0,10)]
print('list1: ', list1)
print(sys.getsizeof(list1))

list2 = [x + y for x in 'abc' for y in '1234']
print(list2)

list3 = [x for x in range(0,10) if x%3 == 0]
print(list3)

list4 = [x if x%3==0 else -x for x in range(0,10)]
print(list4)

# Make words in list5 all lowercase
list5 = ['Apple', 'Banana', 2, 4, 'Hello']
# list6 = [s.lower() for s in list5] dont work cause 'int' dont have lower() method
list6 = [s.lower() if isinstance(s,str) else s for s in list5]
print(list6)

# Generator
generator = (x**2 for x in range(0,10))
print(generator)
for val in generator:
    print(val)
print(sys.getsizeof(generator))

# Change a function into a generator by using 'yield'
def fibGenerator(n = 10):
    a, b = 0, 1
    # _ means it will not be used in the circle
    for _ in range(n):
        a, b = b, a + b
        yield a

for val in fibGenerator(10):
    print(val)

# Use next()
f = fibGenerator()  # One generator object, not a ruturn value
print(f)
print(next(f))  # Call this object
print(next(f))  # Everytime you call the generator, it will excute to the next yield
print(next(f))
print(next(f))
print(next(fibGenerator()))    # A new generator object