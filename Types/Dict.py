Grade = {'Peter':60, 'Jack':63}
print(Grade)
print(Grade['Jack'])

# Use constructor to create dict
dict1 = dict(zip('abc','123'))
dict2 = dict(a = 1, b = 2, c = 3)
print(dict1,dict2)

# Use comprehension  to create dict
dict3 = {num : 2*num for num in range(0,4)}
print(dict3)