T1 = (11,12,"Anuraj",13,10,11,3.14,True) # heterogenous & duplicates is allowed

print(T1)
print(type(T1))
print(T1[0]) # index start from zero
print(T1[-1]) # negative index is allowed

# T1[2] = 20  Not allowed Touple elements is inmuteable

# T1.append(30) # NOt allowed Touple is inmuteable

print("Length of list is : ",len(T1))

# print Touple elements by using For loop
for i in range(0,len(T1),1):
    print(T1[i],end = " ")

print("  ")
# print list elements by using For in loop
for i in T1:
    print(i,end = " ")

print("   ")
# print list elements by using while loop
i = 0
while(i < len(T1)):
    print(T1[i],end = " ")
    i = i + 1