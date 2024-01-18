#매핑 / 맵

#기존 리스트 내 원소들의 합하는 방법
# numbers = ["7", "-11", "3"]
# hap = 0
# for number in numbers:
#     hap += int(number)
# print(hap)

#맵을 사용해서 원소들의 합을 하는 방법
numbers = ["7", "-11", "3"]
print(sum(map(int, numbers)))
#리스트 원소들 전부에 int를 적용한다.