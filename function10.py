# Function as a parameter to another function(callback function)

def Add(value1,value2):
    ans = 0
    ans = value1 + value2
    return ans

def Marvellous(Add,value1,value2):
    print("Inside Marvellous function.")
    iRet = Add(value1,value2)
    print("Addition of this two numbers is : ",iRet)

def main():
    No1 = 10
    No2 = 5

    Marvellous(Add,No1,No2)

if __name__ == "__main__":
    main()