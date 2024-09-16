def studentInfo(Name,R_No,Marks):
    print("Name of Student is : ",Name)
    print("Roll No of student is : ",R_No)
    print("Marks of student is : ",Marks)

def main():
    studentName = input("Enter the name of Student : ")
    rollNum = int(input("Enter the Roll No of Student : "))
    totalMarks = int(input("Enter the Total marks No of Student : "))

    studentInfo(studentName,rollNum,totalMarks)

if __name__ == "__main__":
    main()