
def main():
    Age = int(input("Enter the Numbers to check positive, negative or zero : ")) 
    if(Age > 0):
        print("The Number is Positive.")

    elif(Age < 0):
        print("The Number is Negative.")

    else:
        print("The Number is zero(0)")
if __name__ == "__main__":
    main()