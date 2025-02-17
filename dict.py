# dict is Mutable.
d1 = {'name': 'Ankita', 'age':27, 'phone':2342}
print(d1, type(d1)) 

# In dict we cannot store duplicate keys.
# in dict we can store duplicate values.

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)