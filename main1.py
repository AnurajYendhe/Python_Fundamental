def Addition(No1,No2):
    ans = 0
    ans = No1 + No2
    return ans

def main():
    No1 = 0
    No2 = 0
    iRet = 0
    No1 = int(input("Enter the first Numbers : "))
    No2 = int(input("Enter the second Numbers : "))
    iRet = Addition(No1,No2)
    print("Addition is : ",iRet)