S1 = {11,"Anuraj",13,10,11,3.14,True} # heterogenous & duplicates is NOT allowed

print(S1)
print(type(S1))
print("Length of list is : ",len(S1))
# print(T1[0])  unindex and unorder

# S1[2] = 20  # NOT allowed set elements is unmuteable

S1.add(30) # muteable
print(S1)

S1.remove(13)
print(S1)

S1.discard(10)
print(S1)

# print list elements by using For in loop
for i in S1:
    print(i,end = " ")

print("   ")