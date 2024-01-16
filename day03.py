# 6장 for와 in.

univ = "inha"
i = 0
while i < len(univ):
    print(univ[i], end=' ')
    i += 1

print()

for letter in univ:     # univ 내 특정 구간만을 추출해내고 싶을 때에는 부적절함
    print(letter, end=' ')

print()
# Q. 가끔 교수님 print 하시고 입력하실 때 위에 있는 거 갑자기 끌어오시던데 뭐 단축어가 있는지 ask
#for + range
#for k in range(0, len(univ), 1):
#for k in range(0, len(univ)):
for k in range(len(univ)):    #마지막 인수 1은 1씩 증가하여 추출한다는 의미.
    print(univ[k], end=' ')

'''
결론 : 11번과 같은 코드가 적절함. range 같은 경우는 입력 값이 잘못될 경우 원하는 바를 못 얻을 수 있기 때문
'''

