import array as arr # import array module
def main():
    print("----------Demonstration of array---------")
    a = arr.array('i',[2,4,6,8]) # 'i' is considered as type code
    print("First Element : ",a[0]) # indexing start from 0
    print("Second Elements : ",a[1])
    print("Last Elements : ",a[-1]) # negative index is allowed

    arr1 = arr.array('f',[2.4,4.5,6.5,8.8])
    print(arr1.typecode)

    arr1.reverse()
    print(arr1)

    # for loop on array
    for i in range(0,len(a),1):
        print(a[i])

    # while loop on array 
    i = 0
    while(i < len(a)):
        print(a[i])
        i = i + 1 


if __name__ == "__main__":
    main()