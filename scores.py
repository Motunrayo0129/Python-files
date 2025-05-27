student_score1 = 50
student_score2 = 50
student_score3 = 50
student_score4 = 50

scores = [50, 34, 45, 50, 25]
cart = ['banana', 33, 'juice', 2.5, ['fish', 'palm_oil'], True]

print("We have ", len(cart), "items in cart")
print(cart[4][1])

print("We have ", len(scores), "scores")
print(scores[2])

for score in scores:
	print(scores, end=" ")

print()


for index in range(len(scores)):
	print(index, end="                        ")

for value in enumerate(cart):
	print(value)


print(list(enumerate(cart))[4])

scores.append(99)
#scores.pop(1)
cart[4].insert(0, 6)
print(cart)
#scores.extend([34, 67, 87, 65])
print(scores)
new_list = cart + scores
print(new_list)
print(scores[-1])
print(scores[::2])


