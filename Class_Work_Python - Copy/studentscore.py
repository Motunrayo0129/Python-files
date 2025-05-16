  student_num = int(input('Enter the number of student: '))
top_name = ""
top_score = None
second_top_name =""
second_top_score = None
for score in range(student_num):
	student_name = input("Enter student name: ")
	student_score = int(input("Enter student score: "))

	if top_score is None or score > top_score:
		second_top_score = top_score
		second_top_name = top_name

		top_score = student_score
		top_name = student_name
	elif second_top_score is None or score > second_top_score:
		second_top_score = student_score
		second_top_name = student_name

print(f"{top_name} has the highest score of {top_score} and")
print(f"{second_top_name} has the second highest score of {second_top_score}")