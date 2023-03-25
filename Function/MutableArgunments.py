# In Python, there are mutable type(list, dic...) and immutable type(number, string, tuple)
# Only the objects have type, while variables(including arguments) dont
# Arguments of mutable type will pass the reference, while immutable arguments just pass their value

def change(a):
    print("=====================")
    print("Here is the change function:")
    print(id(a))
    a = 15
    print("change a in the function now")
    print(id(a))
    print("=====================")

def changeList(L):
    print("=====================")
    print("Here is the changeList function:")
    print(id(L))
    L[0] = 3
    print("change L in the function now")
    print(id(L))
    print("=====================")

print("An example of immutable argument passing")
a = 10
print(type(a))
print(id(a))
change(a)
print(a)
print(id(a))

print("=====================")
print("=====================")

print("An example of mutable argument passing")
L = [1, 2, 3]
print(type(L))
print(id(L))
changeList(L)
print(L)
print(id(L))