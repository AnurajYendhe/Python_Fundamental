def squre(n):
    return (n * n)

def main():

    # input list
    arr = [1,2,3,4,5]
    print("Input list is : ",arr)
    
    # empty list to storge result
    result = []

    for i in arr:
        result.append(squre(i))
    
    print("squre of each numbers is : ",result)

if __name__ == "__main__":
    main()