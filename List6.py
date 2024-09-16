data = []
size = int(input("Enter the elements that we want to store : "))
print("Enter the elements : ")

for i in range(0,size,1):
    value = int(input())
    data.append(value)

print("Elements in the list is : ")

for i in range(0,size,1):
    print(data[i])
