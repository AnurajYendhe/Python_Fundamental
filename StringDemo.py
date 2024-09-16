# demonstrain of string

def main():
    Name1 = "Anuraj" # using double quote
    Name2 = 'Yendhe' # using single quote

    print(Name1)
    print(type(Name1))

    print(Name1[0]) # accessing elements by using index
    print(Name1[-1]) # negative indexing is allowed

    print(Name1[0:3]) # print characters in range
    print(Name1[2:5])
    print(Name1[:3])
    print(Name1[2:])

    # Name1[0] = 'X' NOT allowed string are immutable

    print("length of Name1 is : ",len(Name1)) # calculate the length using len() function
    

if __name__ == "__main__":
    main()