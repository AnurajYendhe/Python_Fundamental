def studentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

def main():
    print("Demonstrain of keyword variable numbers of arguments")

    studentInfo(age = 28,address = "Pune", mobile_no = 123,company = "TCS")
    
if __name__ == "__main__":
    main()