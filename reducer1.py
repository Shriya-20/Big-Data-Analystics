#!/usr/bin/env python3
import sys

current_course_id = None
course_name = None
semester = None
students = []

for line in sys.stdin:
    course_id, record = line.strip().split("\t", 1)
    record_type, *values = record.split(",")

    if current_course_id and current_course_id != course_id:
        # Print join results for previous CourseID
        if course_name and semester:
            for student_id, name in students:
                print(f"{student_id}\t{name}\t{course_name}\t{semester}")
        students = []  # Reset student list
        course_name = None
        semester = None

    if record_type == "S":
        students.append(values)  # (StudentID, Name)
    elif record_type == "C":
        course_name, semester = values  # (CourseName, Sem)

    current_course_id = course_id

# Output last set of matches
if current_course_id and course_name and semester:
    for student_id, name in students:
        print(f"{student_id}\t{name}\t{course_name}\t{semester}")

