class FlyingMixin:
	def fly(self):
		return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
	def swim(self):
		return f"{self.name}이(가) 수영을 합니다."

class Pokemon:
	def __init__(self, name):
		self.name = name

class Charizard(Pokemon, FlyingMixin):
	pass

class Gyarados(Pokemon, SwimmingMixin):
	pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(c1.fly())		#하늘을 나는 것만 가져다 씀.
print(g1.swim())





# class Animal:
# 	def says(self):
# 		return 'I speak!'
#
# class Horse(Animal):
# 	def says(self):
# 		return "heee"
#
# class Donkey(Animal):
# 	def says(self):
# 		return "HOooo"
#
# class Mule(Donkey, Horse):
# 	#def says(self):
# 	#return '노새 노새 젊어서 노새~'
# 	pass
#
# class Hinny(Horse, Donkey):
# 	#def says(self):
# 		#return '버새 버새'
# 	pass
# # mule에 있는 says 없으면->Donkey -> Horse->그의 부모인 animal
# m1 = Mule()
# m2 = Hinny()
# print(m1.says())
# print(m2.says())
#
# print(Hinny.__mro__)
