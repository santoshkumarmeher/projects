student_heights = input("Enter the heights of student ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)
total_height=0
for height in student_heights:
    total_height += height
print(total_height)
number_of_student = len(student_heights)
average_height = total_height/number_of_student
print(average_height)
