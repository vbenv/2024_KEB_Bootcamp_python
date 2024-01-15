#Day02_python assignment_12202311_곽성찬

'''
3번을 누르기 전까지 계속 반복되는 무한 루프 만들기
'''

while True:
    number = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
    if number == '1':
        fahrenheit = float(input('Input Fahrenheit: '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    elif number == '2':
        celsius = float(input('Input Celsius: '))
        print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9.0 / 5.0) + 32.0):.4F}F')
    elif number == '3':
        print('프로그램을 종료하겠습니다.')
        break
