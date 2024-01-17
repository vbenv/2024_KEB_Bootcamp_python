# #8장 연습문제
# #8.1
# e2f = dict(dog = 'chien', cat = 'chat', walrus = 'morse')
# print(e2f)
#
# #8.2
# print(e2f['walrus'])
# print(e2f.get('walrus'))
#
# #8.3
# f2e = e2f.items()
# print(f2e)
#
# #8.4
# aa = e2f.keys()
# bb = e2f.values()
# e2f_reverse = dict(zip(bb,aa))
# print(e2f_reverse)
# print(e2f_reverse['chien'])
#
# #8.5
# print(aa)
# print(e2f.keys())
#
# #8.6 이차원 딕셔너리
# life ={
#     'animal' : {'cats' : 'henri', 'octopi' : 'Grumpy', 'emus' : 'Lucy'}
#     , 'plants' : '',
#     'other' : ''}
# #8.7
# print(life.keys())
#
# #8.8
# for i in life['animal'].keys():
#     print(i)
# print(life['animal'].keys())
# #8.9
# print(life['animal']['cats'])
#8.10
#letter_counts = {letter : word.count(letter) for letter in world} #{키_표현식 : 값_표현식 For 표현식 in 객체}
t = []
for i in range(10):
    #print(i)
    q = i**2
    t.append(q)
print(t)
Q = [i**2 for i in range(10)]
print(Q)
squares_keys = [i for i in range(10)]

squares = {squares_keys : i**2 for i in range(10)}
print(squares)
#print(squares)

