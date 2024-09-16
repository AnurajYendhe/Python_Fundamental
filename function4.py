# function accepts mutiple values and return mutiple values
def Arithematic(value1,value2):
    add = value1 + value2
    sub = value1 - value2
    return add,sub
    
def main():
    No1 = 15
    No2 = 10
    iRet = 0
    iRet = Arithematic(No1,No2)
    print("Addition of this two numbers is : ",iRet[0])
    print("Subtraction of this two numbers is : ",iRet[1])

if __name__ == "__main__":
    main()