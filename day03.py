# split 해보기 -> 구분자를 기준으로 하나의 문자열을 여러 개의 리스트로 나눔
course = "2024 KEB Bootcamp"
# print(course)
# list_course = course.split('B')
# print(list_course)
#
# # split으로 응용해보기
# #numbers = input("FirstNumber SecondNumber : ").split()
# #print(numbers[0] + numbers[1])     #concatenation : 연속
# #print(int(numbers[0]) + int(numbers[1]))     #arithmetic operation : 산술 연산
#
# #join : list -> str.
# subjects = ["python", "c++", "database"]
# subjects_string = " / ".join(subjects)
# print(subjects_string)
# print(",".join('abbbcdd'))
#
# #replace('원래 문자', '바꿀 문자', 원하는 바꿀 횟수)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')  # immutable의 원본을 바꾸기 위해서는 재할당을 해줘야 함+ tuple
# print(course)
#
# #원하는 횟수만큼만 바꿀 수 있음.
courses = "* KEB .KEB #KEB !2024 Inha University...*!"
# #print(courses.replace('KEB', 'Inha', 2))


# strip("없애줄 문자들") 양쪽 끝 군더더기들을 지워주는 함수.
print(courses.strip())
print(courses.strip("!#.*"))

#검색 find, rfind, index -> 위치를 알려줌
print(courses.find("KEB"))
print(courses.rfind("KEB"))
print(courses.index("KEB"))

print(courses.find("yahoo"))    # 못 찾으면 '-1'를 출력.
print(courses.index("yahoo"))   # ValueError: substring not found