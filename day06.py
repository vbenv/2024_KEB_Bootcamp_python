class Pokemon:
	def __init__(self, name):
		self.name = name

	def attack(self, target):
		print(f"{self.name}이(가) {target.name}을(를) 공격!")


class Pikachu(Pokemon):		#자식클래스이름(부모클래스이름)
	def __init__(self, name, type):
		super().__init__(name)
		self.type = type
	def attack(self, target):
		print(f"{self.name}이(가) {target.name}을(를) {self.type}공격!")

	def electric_info(self):
		print("전기 계열의 공격")

class Squirtle(Pokemon):		#자식클래스이름(부모클래스이름)
	pass

p1 = Pikachu("피카츄","전기") 	#("이름", "타입")
p2 = Squirtle("꼬부기")
p3 = Pokemon("아무개")
p1.electric_info()
#p3.electric_info()
p1.attack(p2)
p2.attack(p1)

print(p1.name, p1.type)
print(issubclass(Pikachu, Pokemon))		#상속 구조를 확인해볼 때 사용


