i = 1
def fun(No):
    global i 
    if(i < No + 1):
        print("value of i is : ",i)
        i = i + 1
        fun(No)

def main():
    No = 10
    fun(No)

if __name__ == "__main__":
    main()