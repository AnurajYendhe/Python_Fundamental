def main():
    print("Demonstration of Break in loop")

    for i in range(1,11,1):  # without continue
        print(i)

    print("   ")
    for i in range(1,11,1): # with continue 
        if(i == 3):
            continue
        print(i)

if __name__ == "__main__":
    main()