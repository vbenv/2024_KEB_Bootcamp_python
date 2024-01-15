'''
univ = "Inha university"
print(univ)
print(univ[5])
# univ[5] = 'U' // imutable
# print(univ)
subjects = ['python', 'c++', 'linux', 'data structure', 'database']
print(subjects)
print(subjects[3])
subjects[3] = 'data structrue & algorithm' #mutable
print(subjects)
'''

# print(0.1)
# print(1e-1)
# print(0.01)
# print(1e-2)
# print(3.14)
# print(314e-2)
# print(314.1592)
# print(0.3141592e3)
# print(21000)
# print(21_000)

#SyntaxError: cannot assign to literal here
#"univ" = "Inha University" # 리터럴은 보통 오른쪽에 위치.
# 99 = 71 정수형 리터럴

# Ok
# case sensitive
# abc = 7
# 9test = 5
# _9test = 6
# False = 123 reserved word

#숫자
print(type(3.14))
print(type(3.14) == float)
print(isinstance(55, float)) # isinstance(*,type) : 특정 타입의 객체 확인

a = [2,4,99]
b = a
a[0] = 1
print(a)
print(b)

money = 5,000,000
print(money)
print(type(money)) #tuple
cash = 5_000_000
print(cash)
print(type(cash)) #int



base_number = int(input('Input base number : '))
exponent_number = int(input('Input base number : '))
# f-string
#print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {(base_number**exponent_number)}')
#print(f'밑은 {base_number}, 지수는{exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')

#f-function
print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))


