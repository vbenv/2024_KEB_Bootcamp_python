
# 6장 반복문
#prime number
number = int(input("input number : "))
cnt = 0
i = 2
while i < number:
    if number % i == 0:
        cnt += 1
    i += 1
if cnt == 0:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')