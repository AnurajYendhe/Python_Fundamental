import sys  # In sys module there is one tuple name as argv which stroge the commandline Arguments
def main():
    print("Demonstration commandline Arguments.")

    print("Name of File : ",sys.argv[0])  # argv[0] is the name of file by defult
    print("First Arguments : ",sys.argv[1])
    print("Second Arguments : ",sys.argv[2])

if __name__ == "__main__":
    main()