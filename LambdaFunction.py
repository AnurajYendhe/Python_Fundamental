print("--------Demonstrain of array-------")

# Addition
Add = lambda X,Y : X +Y 
No1 = 10
No2 = 11
iRet = Add(No1,No2)
print("Addition is : ",iRet)

# Squre 
Squre = lambda X : X * X
No = 5
iRet = Squre(No)
print("Squre of {} is : ".format(No),iRet)

# power of a numbers 
power = lambda X,Y : X ** Y
No1 = 2
No2 = 3
iRet = power(No1,No2)
print("the",No2,"power of",No1,"is : ",iRet)

# area of squre
Area = lambda X : 4 * X
side = 23
iRet = Area(side)
print("The area of squre is : ",iRet)

# area of circle
AreaCircle = lambda Radius : 3.14 * Radius * Radius
side = 5
iRet = AreaCircle(side)
print("The area of circle is : ",iRet)

