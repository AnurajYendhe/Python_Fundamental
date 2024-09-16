def studentInfo(Name,R_No,Marks = 80): 
    print("Name of Student is : ",Name)
    print("Roll No of student is : ",R_No)
    print("Marks of student is : ",Marks)

def main():
    
    studentInfo(R_No = 31, Marks = 90,Name = "Anuraj")  # we can change the squance of parameter if we call function by using keyWord Arguments
    studentInfo(R_No = 10,Name = "Suyesh")

if __name__ == "__main__":
    main()