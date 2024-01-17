# subjects = ['a','b','c']
subjects = ['a',['b','c'],'d']
# print(subjects[::-1])
# subjects[::-1]
# subjects.reverse() # 리버스 함수는 원본을 바꿈.
# print(subjects)

# #subjects.remove("java")
# #subjects.sort(reverse=True)     # TypeError: '<' not supported between instances of 'int' and 'str'
# subjects.sort(reverse=False) #desc => sort :
# print(subjects)
#
# copy_subjects = sorted(subjects)
# print(subjects)
# print(copy_subjects)

#7.2.23 복사하기
import copy
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(a)
print(subjects, a, b, c, d, e)     #원소 중 immutable한 값을 바꾸면 .copy()만 바뀜
subjects[1][1] ="X"
print(subjects, a, b, c, d, e)     #원소 중 mutable한 값을 바꾸면 전부 바뀐 상태로 적용.

#list comprehension
squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares)

# for i in range(1,6,1):
#     squares.append(i*i)
# print(squares)

# squares = [i*i for i in range(1, 6, 1)]
# print(squares)

even_squares = [i*i for i in range(1, 6, 1) if i % 2 == 0]
print(even_squares)

