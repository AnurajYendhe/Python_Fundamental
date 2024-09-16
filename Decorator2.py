# inbuilt function we can't change it 
def sub(No1,No2):
    return No1 - No2

def SmartSub(fptr):   
    def inner(a,b):
        if(a < b):
            a,b = b,a
        return fptr(a,b)
    return inner

sub = SmartSub(sub)

def main():
    print("-----Demonstration of Decorators in Python------")

    iRet = sub(2,10)
    print("The differance is : ",iRet)
    
if __name__ == "__main__":
    main()