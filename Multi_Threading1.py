import os
import threading

def Task1(value):
    print("all even numbers from 1- 50")
    for i in range(1,51,1):
        if(i % 2) == 0:
            print(i)

def Task2(value):
    print("all odd numbers from 1- 50")
    for i in range(1,51,1):
        if(i % 2) != 0:
            print(i)
    
def main():
    print("----Demonstrain of Multi-Threading ----")
    print("main process id is : ",os.getpid())
    print("Parent process id of main process is : ",os.getppid())
    print("main thread id is : ",threading.get_ident())
    
    No = 5
    t1 = threading.Thread(target = Task1, args = (No,))
    t2 = threading.Thread(target = Task2, args = (No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()