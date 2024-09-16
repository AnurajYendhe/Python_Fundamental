l1 = ["PPA","LB","Python","Angular","LSP"]
l2 = [1800,1900,2000,2100,2200]

print("Elements by using For loop")
for i in range(0,len(l1),1):
    print(l1[i],":",l2[i])
    
print("  ")
print("Elements by using while loop")
i = 0
while(i < len(l1)):
    print(l1[i],":",l2[i])
    i = i + 1