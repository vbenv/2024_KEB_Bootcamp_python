#연습문제
#9.1
# def good() -> list:
#     harry_porter = input().split()
#     return harry_porter
#
# print(good())

#9.2
# def get_odds(n) -> int:
#     '''
#     1부터 n까지의 홀수를 발생시키는 제너레이터
#     :param n: int
#     :return: int
#     '''
#     for i in range(1, n+1, 2):
#         yield i
#
# cnt = 0
# odds = get_odds(10)
# for odd in odds:
#     cnt += 1
#     if cnt == 3:
#         print(f'Third number is {odd}')
#         break

#9.3 open closed principal [OCP]
def test(f):
    """
    데코레이터 함수, 함수 시작하면 start 출력, 끝나면 end 출력
    :param f: function
    :return: closure function
    """
    #def test_in(*args, **kwargs):
    def test_in():
        print('start')
        #result = f(*args, **kwargs)
        f()
        print('end')
        #return result
    return test_in  #closure라서 return

@test
def greeting():
    print("안녕하세요~")

greeting()

# t = test(greeting)    #@test 안 쓸 때 이렇게 호출.
# t()