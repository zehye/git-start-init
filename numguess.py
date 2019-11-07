from random import randint

answer = randint(1,101)
print(answer)

chance = 3
for _ in range(chance):
	guess =int(input("1~100까지 숫자를 고르세요:"))

	if guess == answer:
		print("correct")
		break
	else:
		print("wrong!")
