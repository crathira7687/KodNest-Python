students_count=int(input("enter a students count:"))

passed_count=0
failed_count=0
total_marks=0

for i in range(students_count):
    student_mark=int(input("enter the marks:"))
    total_marks+=student_mark
    if student_mark>40:
        passed_count+=1
    else:
        failed_count+=1
    
print(f"Passed students: {passed_count}")
print(f"Failed students: {failed_count}")
print(f"Total marks: {total_marks}")

if failed_count==0:
    print("Batch Result:All Passed")
else:
    print("Batch Result:Need Improvement")
