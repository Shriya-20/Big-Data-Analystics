#!/usr/bin/env python3
import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 3:
        # Identify if line is from students or courses dataset
        if data[0].isdigit():  # Student record (StudentID, Name, CourseID)
            student_id, name, course_id = data
            print(f"{course_id}\tS,{student_id},{name}")
        else:  # Course record (CourseID, CourseName, Sem)
            course_id, course_name, sem = data
            print(f"{course_id}\tC,{course_name},{sem}")

