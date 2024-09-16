def studentInfo(Name,R_No,Marks = 80):   # defult arguments should be last of arguments list
    print("Name of Student is : ",Name)
    print("Roll No of student is : ",R_No)
    print("Marks of student is : ",Marks)

def main():
    
    studentInfo("Anuraj",31,90)
    studentInfo("Suyesh",10)

if __name__ == "__main__":
    main()