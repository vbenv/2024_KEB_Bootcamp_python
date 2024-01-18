#empty_set 을 만드는 유일한 방법 = set()
#set 으로 list, tuple, dict만들 수 있으나 dict의 경우 key값만 불러옴
#set과 dict은 sequence(순서)가 없음 -> 순서가 중요하지 않을 때 사용
#set은 중복 허용X
# & : set intersection 구할 때 사용. = 변수명.interseciont(다른 변수명)
#| = union() : 합집합.
# - = difference() : 차집합.
# ^ = symmetric_difference() : 대칭 차집합.(두 셋 모두에 포함되지 않는 항목)
#<= = issubset() : 첫번째 셋이 두 번째 셋의 부분집합인지 확인

#set 컴프리헨션
#a_set = {number for number in rage(1,6) if number % 3 == 1} #
#immutable set이 존재. (본래는 mutable) => frozenset() ;읽기 전용
yahoo = {
'wahoo' : {'a','b'},
'wohoo' : {'w','h'},
'iohoo' : {'w','a'}
}
print(not yahoo['wahoo'] & {'h'})