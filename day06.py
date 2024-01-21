# # 10.1 연습문제
# class Thing():
#     pass
#
# example = Thing()
# print(Thing == example)
# print(Thing)
# print(example)
# 결론 : 클래스 띵 / 띵의 객체

# 10.2
class Thing2():
    letter='abc'

print(Thing2.letter)

# 10.3
class Thing3():
    letter = 'xyz'

print(Thing3.letter)
#정답은 NO!

# 10.4
class Element():
        def __init__(self, name, symbol, number):
            self.name = name
            self.symbol = symbol
            self.number = number
#hydrogen = Element('Hydrogen', 'H', 1)
#
# 10.5
el_dict ={'name':'Hydrogen','symbol':'H','number':1}
hydrogen = Element(el_dict['name'],['symbol'],['number'])
print(hydrogen.name)
# 10.6
