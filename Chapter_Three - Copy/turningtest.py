print("What is your problem?")
input() 

print("Have you had this problem before (yes or no)?")
response = input().lower()

if response == "yes":
    print("Well, you have it again.")
elif response == "no":
    print("Well, you have it now.")
else:
    print("Please answer with 'yes' or 'no'.")