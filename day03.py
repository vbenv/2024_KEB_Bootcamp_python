choice = int(input("문제를 골라주세요. \n 1) 화씨를 섭씨로 변환 2) 화씨 또는 섭씨 변환 3)소수 판정 4)구간 소수 5)QUIT\n : "))
#1번 : 화씨 -> 섭씨 변환
if choice == 1:
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')




# 2번 : 화씨 또는 섭씨 변환
if choice == 2:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    else:
        print('Terminate Program.')





# 3번 : 소수 판정
if choice == 3:
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
if choice == 4:
    numbers = input("input first second number : ").split()
    n1 = int(numbers[0])
    n2 = int(numbers[1])

    if n1 > n2:
        n1, n2 = n2, n1

    for number in range(n1, n2+1):
        is_prime = True

        if number < 2:
            pass
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime: print(number, end=' ')

if choice == 5:
    print("Terminate Program")