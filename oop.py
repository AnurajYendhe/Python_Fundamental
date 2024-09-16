class Demo:
    def __init__(self,i,j):
        self.No1 = i 
        self.No2 = j
        
    def Addition(self,i,j):
        self.ans = 0
        self.ans = self.No1 + self.No2
        return self.ans

def main():
    print("------Demonstrain of Object orinted Programming approach(oop)----------")
    No1 = 0
    No2 = 0
    iRet = 0

    No1 = int(input("Enter the first numbers : "))
    No2 = int(input("Enter the second numbers : "))

    obj = Demo(No1,No2)
    iRet = obj.Addition(No1,No2)
    print("Addition of two Numbers is : ",iRet)
if __name__ == "__main__":
    main()