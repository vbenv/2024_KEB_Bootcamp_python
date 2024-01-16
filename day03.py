# 5장 텍스트 문자열

# university = r"Inha\nUniversity!" #raw string
university = "Inha\nUniversity!"
print(university)
number1 = input("First number : ")
number2 = input("Second number : ")
print(number1 + number2) # concatenation:연속
print(number * 3) # duplicate 에러

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'End ' * 2 + '\n'
print(start + middle + end)

letter = 'abcdefghijk'
print(letter[-2]) # 역방향 인뎅싱

# str은 immutable이라 못 바꾸지만 replace, 슬라이스를 이요하여 바꿀 수 있다.
# replace()
name = 'Stanley'
print(name.replace('S', 'e'))
# slice[] -> [a:b] => a<= ~ <b 까지의 숫자 인덱싱
print('H'+name[1:])
print(university[:-11])
print(university[:len(university)])
print(university[:16])
print(university[::2])  # [start : end : step] [::*] 간격이 * 씩 증가

