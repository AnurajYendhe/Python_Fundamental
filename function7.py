# function which contains another nested function define in it.

def OuterFun():
    print("Inside OuterFun function.")
    def InnerFun():
        print("Inside InnerFun function.")
    
    InnerFun()

def main():
    OuterFun()

if __name__ == "__main__":
    main()