
# 6장 반복문
#prime number
number = int(input("input number : "))
cnt = 0
i = 2
while i < number:
    if number % i == 0:
        cnt += 1
        break   #break 하나로 반복 횟수를 줄일 수 있음.
    print(i, end=' ') #몇 번 도는지 보기 위한 확인용 코드
    i += 1

if cnt == 0:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')