student_score=input("Enter Student scores").split()
for i in range (0, len(student_score)):
    student_score[i]=int(student_score[i])
high_score=0
for score in student_score:
    if score > high_score:
        high_score = score
print(f"High score is {high_score}")