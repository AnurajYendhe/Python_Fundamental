class Demo:
    
    No = 10 # class variables

    # constructor in other oop language
    def __init__(self,i,j):
        # inistance variables
        self.No1 = i
        self.No2 = j 

    # inistance method (non-static method in other oop language)
    def Add(self):
        self.ans = 0
        self.ans = self.No1 + self.No2 + Demo.No # inistance method access class variables as well as inistance variables.
        return self.ans
    
    # classmethod (static method in other oop language)
    @classmethod
    def Display(cls):
        print("Inside Display function value of (class variable) No is : ",cls.No) # class method access only class variables.

    # staticmethod
    @staticmethod
    def Fun():
        print("Inside Fun function(static function)") # doesn't access any variables (class and instinace).
       
def main():
    print("------Demonstrain of Instance Method, Class Method and Static Method ----------")
       
    # we can call the class method without using object of a class using name of class.
    Demo.Display()

    # we can call the static method without using object of a class using name of class.
    Demo.Fun()

    # we can call the instance method using object of a class only. 
    obj1 = Demo(10,11)
    iRet = obj1.Add()
    print("Addition of No,No1,No2 is : ",iRet)

    # we can call the class method using object of a class.
    obj1.Display()

    # we can call the static method using object of a class.
    obj1.Fun()

if __name__ == "__main__":
    main()