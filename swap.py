students_morning = 15

students_evening = 25

print(f"Before Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")

students_morning, students_evening = students_evening, students_morning

print(f"After Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")