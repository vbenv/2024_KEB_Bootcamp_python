# prime number
numbers = input("input first second number : ").split()     # -> list 따라서, 여기선 int로 못 바꿈.
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:     #튜플의 패킹 언패킹을 이용하여 첫 숫자가 두번째보다 크더라도 잘 돌아가게 만듦.
    n1, n2 = n2, n1

for number in range(n1, n2+1):  #(,+1)
    is_prime = True

    if number < 2:
        pass    # 아무것도 하지 말고 그냥 넘어가라.
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')

#is_prime? / if is_prime:??? 들여쓰기 안해도 저렇게 되노
