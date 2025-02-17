'''
1.In List we can store Homogeneous as well as Heterogeneous Data.
2.Inlist we can store Duplicate Values.
3.List is an Ordered Collenction of Data: Order of insertion will remain
as it is in the output.
4.Lists are Mutalbe: Once we declare the list we can modify it.


'''

li1 = [10, 20, 44, 45, True, 'Kodnest', 20]
print(li1, type(li1)) 


#append(): Will add element at the end of the list
li1.append(300)#[10, 20, 44.45, True, Kodnest, 20, 300]
print(li1)


#insert(index, element)
li1.insert(1, 15)
print(li1) 


#remove(ele): Remove the first occurence of the specified ele.
li1.remove(20)
print(li1) #[10, 15, 44.45, true, 'kodnest', 20, 300]

#in and not in Operator:

print(2000 in li1) #false
print('kodnest' in li1)#True

#pop():Without argument will delete and retrun last ele. from list
removed_ele =li1.pop()
print(removed_ele)#300
print(li1)#[10, 15, 44.45, True, 'Kodnest', 20]


#pop(index): With argument will delete the ele. at specified index
removed_ele = li1.pop(4)
print(removed_ele) # Kodnest
print(li1) #[10, 15, 44.45,true]


# del kayword:
del li1[1]
print(li1)#[10, 44.45, True, 20]

del li1
print(li1)#Error:name 'Li1' is not define



