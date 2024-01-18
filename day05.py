#Chapter 9. Function
# def : 함수가 하는 일 1. 매개변수 정의하기     2. 결과 호출하기
# 함수 이름 정할 때 가독성이 좋게 짜자. 결과값이 어떻게 나올지 예측 가능한 이름!
#함수는 독립적인 코드.

def isprime(n) -> bool:     #함수 다음 -> 'type' : 타입명을 명시해줄 수 있음. 없어도 잘 돌아감.
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """     #함수가 어떤 매뉴얼이 있는지 document를 달아두는거다. => help(isprime): 로 확인 가능
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    if isprime(number):     #prime이 맞는지 확인하기 위한 함수.
        print(number, end=' ')