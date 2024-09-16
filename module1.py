import userDefineModule1

def main():
    No1 = 0
    No2 = 0
    iRet = 0
    No1 = int(input("Enter the first Numbers : "))
    No2 = int(input("Enter the second Numbers : "))
    iRet = userDefineModule1.Addition(No1,No2)
    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()