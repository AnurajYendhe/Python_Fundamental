class HDFC:
    
    ROI = 10.5 # class variables

    # constructor in other oop language
    def __init__(self,Name,Balance):
        # inistance variables
        self.AccountHOLDER = Name
        self.Balance = Balance

    # inistance method (non-static method in other oop language)
    def DisplayBalance(self):
        print("Hi {}".format(self.AccountHOLDER))
        print("Your current Balance is : ",self.Balance)
    
    def Deposite(self,amount):
        self.Balance = self.Balance + amount
        self.DisplayBalance()

    def WithDraw(self,amount):
        if(amount > self.Balance):
            print("There is No sufficient Balance in Your Account")
        else:
            self.Balance = self.Balance - amount
            self.DisplayBalance()

    # classmethod (static method in other oop language)
    @classmethod
    def DisplayBankInfo(cls):
        print("Our Bank is international bank.")
        print("Our Rate of Interst(ROI) is : ",cls.ROI) # class method access only class variables.

    # staticmethod
    @staticmethod
    def DisplayKYCInfo():
        print("Adhar card and Pan card") # doesn't access any variables (class and instinace).
        print("Passport size photos")
         
def main():

    Anuraj = HDFC("Anuraj",20000)
    Anuraj.DisplayBalance()
    Deposite = int(input("Enter the amount that we want to Deposite : "))
    Anuraj.Deposite(Deposite)
    WithDraw = int(input("Enter the amount that we want to withDraw : "))
    Anuraj.WithDraw(WithDraw)
    Anuraj.DisplayBankInfo()
    Anuraj.DisplayKYCInfo()

    Suyesh = HDFC("Suyesh",30000)
    Suyesh.DisplayBalance()
    Deposite = int(input("Enter the amount that we want to Deposite : "))
    Suyesh.Deposite(Deposite)
    WithDraw = int(input("Enter the amount that we want to withDraw : "))
    Suyesh.WithDraw(WithDraw)
    Suyesh.DisplayBankInfo()
    Suyesh.DisplayKYCInfo()

if __name__ == "__main__":
    main()