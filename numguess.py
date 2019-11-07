from random import randint

answer = randint(1,101)
print(answer)

guess =int(input("1~100까지 숫자를 고르세요:"))

if guess==answer:
	print(">>>>>맞았습니다")
else:
	print(">>>>>틀렸지롱")
