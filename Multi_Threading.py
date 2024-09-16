import os
import threading

def Task1(value):
    print("Executing the Task1...")
    print("Process id of running process for Task1 is : ",os.getpid())
    print("Parent Process id of running process for Task1 is : ",os.getppid())
    print("Thread id of Task1 thread is : ",threading.get_ident())
    print("The Name of Task1 Thread is : ",threading.current_thread())

def Task2(value):
    print("Executing the Task2...")
    print("Process id of running process for Task2 is : ",os.getpid())
    print("Parent Process id of running process for Task2 is : ",os.getppid())
    print("Thread id of Task2 thread is : ",threading.get_ident())
    print("The Name of Task2 Thread is : ",threading.current_thread())
    
def main():
    print("----Demonstrain of Multi-Threading ----")
    print("main process id is : ",os.getpid())
    print("Parent process id of main process is : ",os.getppid())
    print("main thread id is : ",threading.get_ident())
    print("The Name of main Thread is : ",threading.current_thread())
    
    No = 5
    t1 = threading.Thread(target = Task1, args = (No,))
    t2 = threading.Thread(target = Task2, args = (No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()