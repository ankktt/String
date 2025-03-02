li1 = [1,2,3,4,5]
print(li1)
sq_li = []
for i in li1:
    sq_li.append(i**2)
print(sq_li)

#List Comprehension:
#[expression for i in iterable_object conditoin]

li1 = [1, 2, 3]
new_li1 = [i for i in li1] #[1, 2, 3]
sq_li1 = [i**2 for i in li1] #[1, 4, 9]
new_li = [ele + 2 for ele in li1] #[3, 4, 5]


li1 = [1, 2, 3, 4, 5]
even = [i for i in li1 if i % 2 == 0] [2, 4]
print(even) # [2, 4]

#When we have onlu if part then write it after for loop.
even = [i for i in  li1 if i %2 == 0]
sq_list = [i**2 for i in li1]
new_li1 = [ele+2 for ele in li1] 

#When we have if-else both write it before for loop
even_odd = ['even' if i % 2 == 0 else 'Odd' for i  in li1] 

#Nested for loops inside list comprehension
# or multiple for loop Inside List Comprehension
li = [[10,20], [30, 40], [50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li) #[10, 20, 30, 40, 50, 60]




[(i, j, k) for i in range(r1 + 1) for j in range(r2+1) for k in range(r3+1) if i+j+k != 2]