from functools import reduce

def main():
    arr = list()
    for i in range(1,21,1):
        arr.append(i)

    print("the original list is : ",arr)

    filter_output = list(filter(lambda No: No % 2 == 0,arr))
    print("List after filter : ",filter_output)

    map_output = list(map(lambda No : No + 2,filter_output))
    print("List after Map :",map_output)

    result = reduce(lambda A,B : A + B,map_output)
    print("result after reduce : ",result)


if __name__ == "__main__":
    main()