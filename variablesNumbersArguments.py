def Sum(*No):
    total = 0
    for i in No:
        total = total + i 
        
    return total
def main():
    iRet = Sum(10,11,12,13)
    print("Sum of this numbers is : ",iRet)

    iRet = Sum(14,15,16,17,18,19,20,21,22) # we can pass multiple numbers of parameter
    print("Sum of this numbers is : ",iRet)
    
if __name__ == "__main__":
    main()