# inbuilt function we can't change it 
def sub(No1,No2):
    return No1 - No2

#decorator
def SmartSub(fptr):   
    def inner(a,b):
        if(a < b):
            a,b = b,a
        return fptr(a,b)
    return inner



def main():
    print("-----Demonstration of Decorators in Python------")

    No1 = int(input("Enter the first Number : "))
    No2 = int(input("Enter the second Number : "))

    subx = SmartSub(sub)

    iRet = subx(No1,No2)
    print("The differance is : ",iRet)
    
if __name__ == "__main__":
    main()