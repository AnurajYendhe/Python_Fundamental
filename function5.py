# function accepts mutiple values and return mutiple values
def Arithematic(value1,value2):
    add = value1 + value2
    sub = value1 - value2
    return add,sub
    
def main():
    No1 = 15
    No2 = 10
    iRet1 = 0
    iRet2 = 0
    iRet1,iRet2 = Arithematic(No1,No2)
    print("Addition of this two numbers is : ",iRet1)
    print("Subtraction of this two numbers is : ",iRet2)

if __name__ == "__main__":
    main()