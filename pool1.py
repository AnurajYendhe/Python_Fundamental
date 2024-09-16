import os
import multiprocessing

def squre(n):
    print("Worker process id for {0}: {1}".format(n,os.getpid()))
    return (n * n)

def main():

    # input list
    arr = [1,2,3,4,5]
    print("Input list is : ",arr)
    
    # creating a pool object
    p = multiprocessing.Pool()

    # map list to target function
    result = p.map(squre,arr)
    print("squre of each numbers is : ",result)

if __name__ == "__main__":
    main()