class FlyingMixin:
	def fly(self):
		return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
	def swim(self):
		return f"{self.name}이(가) 수영을 합니다."

class Pokemon:
	def __init__(self, name):
		self.name = name

	def attack(self):
		print("공격")

	def get_name(self):
		return self.name

	def set_name(self, new_name):
		self.name = new_name
class Charizard(Pokemon, FlyingMixin):
	pass

class Gyarados(Pokemon, SwimmingMixin):
	pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(c1.fly())		#하늘을 나는 것만 가져다 씀.
print(g1.swim())
c1.attack()
Charizard.attack(c1)	#클래스명.함수(객체)

print(g1.get_name())
g1.set_name("잉어킹")
print(g1.name)

