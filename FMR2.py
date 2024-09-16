from functools import reduce

Even = lambda No: No % 2 == 0

increase = lambda No : No + 2

Total = lambda A,B : A + B

def main():
    arr = list()
    for i in range(1,21,1):
        arr.append(i)

    print("the original list is : ",arr)

    filter_output = list(filter(Even,arr))
    print("List after filter : ",filter_output)

    map_output = list(map(increase,filter_output))
    print("List after Map :",map_output)

    result = reduce(Total,map_output)
    print("result after reduce : ",result)


if __name__ == "__main__":
    main()