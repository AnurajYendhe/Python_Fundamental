from functools import reduce

def Even(No):
    if(No % 2) == 0:
        return No

def increase(No):
    ans = No + 2
    return ans

def Total(A,B):
    ans = A + B
    return ans

def main():
    arr = list()
    Size = int(input("Enter the size of list : "))
    print("Enter the elements : ")
    for i in range(0,Size,1):
        value = int(input())
        arr.append(value)

    print("the original list is : ",arr)

    filter_output = list(filter(Even,arr))
    print("List after filter : ",filter_output)

    map_output = list(map(increase,filter_output))
    print("List after Map :",map_output)

    result = reduce(Total,map_output)
    print("result after reduce : ",result)


if __name__ == "__main__":
    main()