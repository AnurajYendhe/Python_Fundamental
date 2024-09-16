# Function define another function inside it.


def Marvellous():
    def Add(value1,value2):
        return value1 + value2
        
    return Add

def main():
    No1 = 10
    No2 = 5
    iRet = 0
    iRet = Marvellous()
    ans = iRet(No1,No2)
    print("Addition is : ",ans)

if __name__ == "__main__":
    main()