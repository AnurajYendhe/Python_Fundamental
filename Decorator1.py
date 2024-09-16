# inbuilt function we can't change it 
def sub(No1,No2):
    return No1 - No2

def SmartSub(No1,No2):
    if(No1 < No2):
        No1,No2 = No2,No1

    return sub(No1,No2)
    
def main():
    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    iRet = SmartSub(No1,No2)
    print("The differance is : ",iRet)
    
if __name__ == "__main__":
    main()