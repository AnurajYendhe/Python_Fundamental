import sys  # In sys module there is one tuple name as argv which stroge the commandline Arguments
def main():
    print("commandline Arguments for addition of two numbers")

    print("Name of File : ",sys.argv[0])  # argv[0] is the name of file by defult
    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    ans = No1 + No2
    print("Addition of this two numbers is : ",ans)

if __name__ == "__main__":
    main()