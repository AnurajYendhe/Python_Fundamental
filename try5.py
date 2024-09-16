def Division(No1,No2):
    try:
        ans = No1 / No2

    except ZeroDivisionError as zobj:
        print("Error : divider zero is not allowed",zobj)
        return
    
    finally:
        print("Thank you for using this Application.")

    return ans
def main():
    try:
        divident = int(input("Enter the divident : "))
        divider = int(input("Enter the divider : "))

        quotient = Division(divident,divider)

    except ValueError as obj:
        print("Error : Invalid inputs",obj)
        return

    except Exception as Err:  
        print("Error : something is worng",Err)
        return

    finally:  # it is optional
        print("Thank you for using this Application.")
        
    print("Division of two numbers",quotient)

if __name__ == "__main__":
    main()