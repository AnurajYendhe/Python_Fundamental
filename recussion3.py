import sys

def main():
    print("Maximun number of recussion call are : ",sys.getrecursionlimit())

    # we can change recussion limits
    # sys.setrecursionlimit(1500)
    # print("Maximun number of recussion call are : ",sys.getrecursionlimit())

if __name__ == "__main__":
    main()