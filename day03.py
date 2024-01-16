#6장반복문
# prime number
number = int(input("input number : "))

is_prime = True
if number < 2:
    print(f'{number} is NOT prime number!')
else:
    for i in ragne(2, number):
        if number % i == 0:
            is_prime = False
            break


    if is_prime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number!')
