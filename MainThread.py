import os
import threading
def main():
    print("----Demonstrain of single thread and single process ----")
    print("Every Program which have one Process(main process) and one Thread(main thread)")
    print("Current process id is : ",os.getpid())
    print("Current thread id is : ",threading.get_ident())

if __name__ == "__main__":
    main()