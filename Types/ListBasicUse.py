list1 = [1, 2, 3, 4, 5]
print('list1: ', list1)
# Use index
print('list1[1]: ', list1[1])
print('list1[4]: ', list1[4])
print('list1[-1]: ', list1[-1])
print('list1[-5]: ', list1[-5])
# Use the minus index to reverse the list
list2 = list1[::-1]
print('list2 = list1[-1:-5]: ', list2)

# Traverse the list
for index in range(len(list1)):
    print(list1[index])
for elem in list1:
    print(elem)
for index, elem in enumerate(list1):
    print(f'{index}, {elem}')

# Some methods
list1.append(100)
print("list1.append(100): ", list1)

list1.insert(1, 200)
print("list1.insert(1, 200): ", list1)

if 1 in list1:
    list1.remove(1)
    print("list1.remove(1): ", list1)

list1.pop(1)
print("list1.pop(1): ", list1)

list1.clear()
print(list1)