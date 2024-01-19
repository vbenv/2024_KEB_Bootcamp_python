# class Pokemon():
class Pokemon:
	def __init__(self, name): # self는 기본값. 그 뒤에 변수
		self.name = name
		print(f"{name} 포켓몬스터 생성")

	def attack(self, target):
		print(f'{self.name}이(가) {target.name}을(를) 공격!')

charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
print(pikachu.name)
charizard.attack(squirtle)
#해당 객체마다 단 한번만 태어날 수 있음.
#이 프로그램이 끝나면 객체는 소멸됨
# pikachu.name = ("피카츄")
# pikachu.nemesis = squirtle
# print(pikachu.name)
# print(pikachu.nemesis) #객체를 어떻게 출력할지 안정해줌
# pikachu.nemesis.name = "꼬부기"#squirtle.name = ("꼬부기")
# print(squirtle.name)
#
