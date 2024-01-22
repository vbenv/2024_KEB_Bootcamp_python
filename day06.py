#포켓몬 게임 만들기
import random

user_name = input("당신의 닉네임을 적어주세요 : ")
print(f"안녕하세요 {user_name}님 포켓몬 세상에 오신 것을 환영합니다.")
# class Character():
#     def __init__(self,name):
#         self.name = name
#         return (f"안녕하세요 {name}님 포켓몬 세상에 오신 것을 환영합니다.")
player = input("당신의 캐릭터를 1~3번 중에 골라주세요.")
if player == '1':
    player = "루피"
    print("당신은 루피를 고르셨습니다.")
if player == '2':
    player = "나미"
    print("당신은 나미를 고르셨습니다.")
if player == '3':
    player = "우솝"
    print("당신은 우솝을 고르셨습니다.")


class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.__name = name

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    def __add__(self, target):
        return return f"두 포켓몬스터 체력의 합은 {self.hp + target.hp} 입니다."
   # name = property(get_name, set_name)


class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")

# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.get_name())

# property 3nd
#print(g1.name)
# print(g1.__name) #direct는 안되고 프로포티로만 가능.
#print(g1._Pokemon__name) #직접 접근이 아니라 우회해서 접근.
#g1.__name = "잉어킹" # 안된다
#g1._Pokemon__name = "잉어킹" #객체.클래스명__함수 로 접근 가능하다.
#print(g1._Pokemon__name) #사실상 private개념은 없는 걸로