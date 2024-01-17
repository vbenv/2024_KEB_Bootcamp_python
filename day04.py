# Assignment (add prime series program)

#현재 이 코드의 문제점
#1. 효율의 문제(3,4) => 2로 나눴을 때 2의 곱셈들은 다 빼고 돌리면 됨.
#2. 소수 판정 식에 소수 판정하는 데 중복되는 부분 있음
#3. 4번 구간소수 인풋의 사용에 대한 설명 부족
#4. 4번 숫자 두 개 입력하고 정의내리는 5줄을 가독성, 간결하게 해낼 수 있음.

choice = int(input("문제를 골라주세요. \n 1) Fahrenheit -> Celsius 2) Celsius -> Fahrenheit 3) Prime1 4) Prime 2 5)QUIT\n : "))
# 1번 : 화씨 -> 섭씨 변환
if choice == 1:
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

# 2번 : 화씨 또는 섭씨 변환
elif choice == 2:
    celsius = float(input('Input Celsius : '))
    print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0) + 32.0):.4f}F')



# 3번 : 소수 판정
elif choice == 3:
    number = int(input("input number : "))
    is_prime = True
    if number < 2:
        print(f'{number} is NOT prime number!')
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')

# 4번 : 구간소수
elif choice == 4:
    numbers = input("input first second number : ").split()
    n1 = int(numbers[0])
    n2 = int(numbers[1])

    if n1 > n2:
        n1, n2 = n2, n1

    for number in range(n1, n2 + 1):
        is_prime = True

        if number < 2:
            continue #pass
        else:
            i = 2
            while i*i < number: # performance issue
                if number % i == 0:
                    is_prime = False
                    break
                i += i
            if is_prime:
                pass
                print(number, end=' ')
    print()
if choice == 5:
    print("Terminate Program")