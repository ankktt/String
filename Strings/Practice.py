print(bool('Kodnest')) #True
#print(int('kod')) #Error
print(int('11')) #11 ---> IMP Str(int) --->INT
#print(float(kodnest)) # Error
print(float('22.22')) #22.22 --->
print(bool(''))#false
print(bool(0)) #false
print(bool(12)) #true
print(int(12.56)) #12

#Taking floating value from user and converting it into int
value = int(float(input('Enter price: Float value')))
print(value, type(value))