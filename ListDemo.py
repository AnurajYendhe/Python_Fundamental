l1 = [10,11,12,13,14,15,16,17] 
print(l1)
print("Length of list is : ",len(l1))
print(type(l1))

print(l1[0]) # index start from zero
print(l1[-1]) # negative index is allowed

l1[2] = 20 # list elements is muteable
print(l1)

l1.append(30) # list is muteable
print(l1)

l1.remove(15)
print(l1)

print(l1[1:])
print(l1[:3])

l1.insert(3,50)
print(l1)

l1.pop()
print(l1)


# print list elements by using For loop
for i in range(0,len(l1),1):
    print(l1[i],end = " ")
print("  ")

# print list elements by using For in loop
for i in l1:
    print(i,end = " ")
print("  ")

# print list elements by using while loop
i = 0
while(i < len(l1)):
    print(l1[i],end = " ")
    i = i + 1


list2 = [11,12,"Anuraj",13,10,11,3.14,True] # heterogenous & duplicates is allowed
print(list2)

# we can create list of lists

data1 = [10,20,30,40,50]
data2 = [60,70,80,90,100]

data = [data1,data2]
print(data)