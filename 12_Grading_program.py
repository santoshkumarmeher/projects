student_score={
    "Harry":85,
    "Ron":75,
    "Hermione":65,
    "Draco":55,
    "Neville":45
}
student_grade={ }
for student in student_score:
    grade=student_score[student]
    if grade>=90:
        print(f"{student} is Outstanding")
    elif grade>=80:
        print(f"{student} is Exceed Expectation")
    elif grade>=70:
        print(f"{student} is acceptable")
    elif grade>=60:
        print(f"{student} is Good")
    else:
        print(f"{student} is Fail")
