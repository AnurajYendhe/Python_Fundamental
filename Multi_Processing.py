import os
import multiprocessing

def Task1(value):
    print("Executing the Task1...")
    print("Process id of running process for Task1 is : ",os.getpid())
    print("Parent Process id of running process for Task1 is : ",os.getppid())

def Task2(value):
    print("Executing the Task2...")
    print("Process id of running process for Task2 is : ",os.getpid())
    print("Parent Process id of running process for Task2 is : ",os.getppid())
    
def main():
    print("----Demonstrain of Multi-Processing ----")
    print("main process id is : ",os.getpid())
    
    No = 5
    p1 = multiprocessing.Process(target = Task1, args = (No,))
    p2 = multiprocessing.Process(target = Task2, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()