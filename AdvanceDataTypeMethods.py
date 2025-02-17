li1 = list('kod')
print(li1)

li2 = list((10,20))
print(li2) # [10, 20]

li3 = list({100, 200})
print(li3)

li4 = list({100, 200})
print(li4)

li4 = list({'Name':'Priya', 'age' : 22})

print(li4)

li5 = list(range(1, 11)) 
print(li5)

#tuple(iterable_object)
tup1 = tuple([10, 20, 30])
print(tup1)
tup2 = tuple({100, 200})
print(tup2)

tup3 = tuple(range(1,11))
print(tup3)
tup4 = tuple('Kodnest')
print(tup4)

tup5 = tuple({'name':'Priya', 'age': 22})
print(tup5)


s1 = set([10, 20, 20, 30])
print(s1)


#set (iterable_object : key : value):
d1 = dict([['name','priya'], ['age', 22]])
print(d1)
