
def main():
    
    divident = int(input("Enter the divident : "))
    divider = int(input("Enter the divider : "))

    try:
        quotient = divident / divider

    except ZeroDivisionError as zobj:
        print("Error : divider zero is not allowed",zobj)
        return

    print("Division of two numbers",quotient)

if __name__ == "__main__":
    main()