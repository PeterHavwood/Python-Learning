# Tuple is a immutable type, so you can not change its elements
# When you change a tuple, you will change the object that the variable refers to

# Use () instead of [] to define a tuple
import sys


tuple1 = (1, 2, 3)
print(tuple1)
print(tuple1[1])

# tuple[1] = 3 is forbidden
tuple1 = (1, 3, 3) # Now tuple1 refers to a new object of tuple type

list1 = [1, 2, 3]
# Tuple takes less memory space and run faster than list when they have the same elements
print('The size of tuple1 is ', sys.getsizeof(tuple1))
print('The size of list1 is ', sys.getsizeof(list1))