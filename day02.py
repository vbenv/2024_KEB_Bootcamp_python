'''
print("univ" == "Inha University")

# = 할당 assignment
# 오른쪽의 값을 왼쪽에 대입한다
a = 3
print(a == 3)
# == 조건 연산자
# 무조건 bool 연산
print(divmod(100,6))
print(-5**3)
print(-(5**2))
print((-5)**2)
artists = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artists
print(artists, groups)
artists[2] = '세븐틴'
print(artists, groups)

print(int(True))
print(float(True))

second_per_hour=(60*60, ': 1hour')
print(second_per_hour*24, ": 하루")
'''


while True:
    number = int(input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : "))
    if number == 1:
        fahrenheit = float(input('Input Fahrenheit: '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    elif number == 2:
        celsius = float(input('Input Celsius: '))
        print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9.0 / 5.0) + 32.0):.4F}F')
    elif number == 3:
        print('프로그램을 종료하겠습니다.')
        break
