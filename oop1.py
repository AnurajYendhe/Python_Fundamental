class Demo:
    # class variables
    No = 10

    # constructor in other oop language
    def __init__(self,i,j):
        # inistance variables
        self.No1 = i
        self.No2 = j 
       
def main():
    print("------Demonstrain of Class variable ----------")
    
    # we can access the class variables without using object of a class using name of class
    print("Value of No for Demo class is : ",Demo.No)

    obj1 = Demo(10,11)
    # we can access the class variables using object of a class 
    print("value of No for obj1 is : ",obj1.No)

    # we can reassign the value of class variable by using name of class it's apply for all the object
    Demo.No = 11
    print("Value of No for Demo class is : ",Demo.No)

    # we can also change the value of class variable by using object of class it's apply that object only
    obj1.No = 15
    print("value of No for obj1 is : ",obj1.No)

    # for other objects the value of class variables remance same
    obj2 = Demo(21,51)
    print("value of No for obj2 is : ",obj2.No)


if __name__ == "__main__":
    main()