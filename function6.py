# function which calls another function which is define outside it.

def Outer2():
    print("Inside Outer2")
    
def Outer1():
    print("Inside Outer1.")
    Outer2()

def main():
    Outer1()

if __name__ == "__main__":
    main()