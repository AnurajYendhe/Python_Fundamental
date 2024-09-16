def main():
    print("Demonstration of Break in loop")

    for i in range(1,6,1):  # without break
        print(i)

    print("   ")
    for i in range(1,6,1): # with break 
        if(i == 3):
            break
        print(i)

if __name__ == "__main__":
    main()