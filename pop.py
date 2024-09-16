def Addition(i,j):
    ans = 0
    ans = i + j
    return ans

def main():
    print("------Demonstrain of Procedural Programming approach(pop)----------")
    No1 = 0
    No2 = 0
    iRet = 0

    No1 = int(input("Enter the first numbers : "))
    No2 = int(input("Enter the second numbers : "))

    iRet = Addition(No1,No2)
    print("Addition of two Numbers is : ",iRet)
if __name__ == "__main__":
    main()