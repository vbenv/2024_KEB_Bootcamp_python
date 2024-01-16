#2번 과제. 연습문제 143P.

#6.1 for 문으로 리스트[3,2,1,0]를 출력
# list = [3,2,1,0]
# for i in list:
#     print(i)


'''
6.2 guess_me 변수에 7을 할당하고, number 변수에 1을 할당한다. 
number와 guess_me 를 비교하는 while 문을 작성해보자. 
number가 guess_me보다 작으면 ' too Low'를 출력 한다. 
number와 guess_me가 같으면 'found it!'을 출력하고 반복문을 종료한다. 
number 가 guess_me보다 크면 'oops'를 출력하고 반복문을 종료한다. 
그리고 반복문의 마지막에 number를 1씩 증가시킨다.
'''
# guess_me = 7
# number = 1
#
# while True:
#     if number < guess_me:
#         print("'too Low'")
#         number += 1
#     elif number == guess_me:
#         print("'foud it!'")
#         break
#     else:
#         print("'oops")
#         break





'''
6.3 guess_me 변수에 5를 할당하고, for 문을 사용하여 range(10)에서 number 변수를 사용 한다. 
number가 guess_me보다 작으면 too low를 출력한다. number와 guess_me가 같으면 found it!'을 출력하고 반복문을 종료한다. 
number 가 guess_me보다 크면 0ops'를 출력하고 반복문을 종료한다.
'''

# guess_me = 5
# for number in range(10):
#     if number < guess_me:
#         print("'too Low'")
#         print(number)
#     elif number == guess_me:
#         print("'foud it!'")
#         continue
#     else:
#         print("'oops")
#         break
