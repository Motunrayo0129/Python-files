print(""" Press the option below in interger
1. Add a task.
2. view task. 
3. Mark task as complete.
4. Delete a task
5. Exit. """) 

option = int(input("Enter a number: "))
if option == 1:
	user_input = input("Enter an item: ")
	print("Task added")
elif option == 2:
	print("No tasks input")
elif option == 3:
	print("(.) task completed")
elif option == 4:
	print("task successfully deleted")
elif option == 5:
	print("Exit")
else:
	print("Invalid input")



	
	

