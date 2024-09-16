
def main():
    try:
        divident = int(input("Enter the divident : "))
        divider = int(input("Enter the divider : "))

        quotient = divident / divider

    except ZeroDivisionError as zobj:
        print("Error : divider zero is not allowed",zobj)
        return

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