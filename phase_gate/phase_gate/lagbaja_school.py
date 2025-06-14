student_count = int(input("Enter the number of students: "))
subject_count = int(input("Enter the number of subjects: "))

student_scores = [[0] * subject_count for _ in range(student_count)]
total_student_scores = [0] * student_count
total_subject_scores = [0] * subject_count
subject_failure_count = [0] * subject_count

hardest_subject = 0
easiest_subject = 0
best_student = 0
worst_student = 0

for student_index in range(student_count):
    print(f"Entering scores for Student {student_index + 1}:")
    
    for subject_index in range(subject_count):
        while True:
            try:
                score = int(input(f"Enter score for Subject {subject_index + 1} (0-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("Invalid input! Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        student_scores[student_index][subject_index] = score
        total_student_scores[student_index] += score
        total_subject_scores[subject_index] += score

        if score < 50:
            subject_failure_count[subject_index] += 1

for subject_index in range(subject_count):
    if subject_failure_count[subject_index] > subject_failure_count[hardest_subject]:
        hardest_subject = subject_index
    if subject_failure_count[subject_index] < subject_failure_count[easiest_subject]:
        easiest_subject = subject_index

for student_index in range(student_count):
    if total_student_scores[student_index] > total_student_scores[best_student]:
        best_student = student_index
    if total_student_scores[student_index] < total_student_scores[worst_student]:
        worst_student = student_index

print("SUBJECT SUMMARY:")
print("==========================================================================")
for subject_index in range(subject_count):
    print(f"Subject {subject_index + 1}:")
    print(f"Total Score: {total_subject_scores[subject_index]}")
    print(f"Number of Fails: {subject_failure_count[subject_index]}")
    print("======================================================================")

print("CLASS ANALYSIS:")
print("==========================================================================")
print(f"Hardest Subject: Subject {hardest_subject + 1} with {subject_failure_count[hardest_subject]} failures.")
print(f"Easiest Subject: Subject {easiest_subject + 1} with {student_count - subject_failure_count[easiest_subject]} passes.")
print("==========================================================================")

print("STUDENT PERFORMANCES:")
print("==========================================================================")
print(f"Best Graduating Student: Student {best_student + 1} scoring {total_student_scores[best_student]}")
print("==========================================================================")
print()
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f"Worst Graduating Student: Student {worst_student + 1} scoring {total_student_scores[worst_student]}")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print()
print("==========================================================================")