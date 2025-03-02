'''
1. In set we can store Homogeneous as well as Heterogeneous data.

2. Set is an Unordered Collection of Data.

3. Set does not support indxing of data.
4. In set we canot store duplicates.
5. setes are mutable.


'''


s1 = {10, True, 'kodnest', 10, 20, 55.44}
print(s1, type(s1)) #{True, 20, 55.44, 10, kodnest}
#print(s1[0])#error


print(s1, type(s1))
#add(): Used to add an element in the set
s1.add(500)
print(s1)

s1.remove(55.44)
print(s1)#{True , 20, 500, 10, 'Kodnest'}

#pop() : Without index will delete and return one ele.
poped_ele = s1.pop()
print(poped_ele)#True
print(s1)#{20, 500, 10, 'kodnest}