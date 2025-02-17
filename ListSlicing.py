
li1 = [10, 20, 30, 40, 50, 60]
sub_list = li1[0:4:1]
print(sub_list)

sub_list2 = li1[1::]
print(sub_list2)

sub_list3 = li1[::2]
print(sub_list3)

reverse_li1 = li1[::-1]
print(reverse_li1)

print(li1[-1::])



'''
Q. What is List Slicing?
Is Used to create sublist from main list.
Syntax: list_name [start: end - 1: steps]

reverse list: [::-1]
last ele: [-1::]

'''

