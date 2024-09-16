# Function accepts multiple parameter and call another functin in it

def Add(value1,value2):
    return value1 + value2

def Sub(value1,value2):
    return value1 - value2

def Marvellous(value1,value2):
    print("Inside Marvellous function.")
    ans = Add(value1,value2)
    print("Addition is : ",ans)

    ans = Sub(value1,value2)
    print("Subtraction is : ",ans)

def main():
    No1 = 10
    No2 = 5
    
    Marvellous(No1,No2)

if __name__ == "__main__":
    main()