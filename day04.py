#8chapter "dict, set"
sugang = dict(python = "kim", cpp = "sung", db = "kang")
# print(sugang)
# sugang["datastructure"] = 'kim' # add
# print(sugang)
# sugang["datastructure"] = 'park'    # update
# print(sugang)
# print(sugang['db'])     #[key]
# print(sugang.get('db')) #get()
# print(sugang.get('ooo', 'not exist')) #get (키, none 출력어 설정)
for subject, professor in sugang.items():
    print(f'{subject} 과목 담당교수는 {professor}입니다.')

for s in sugang.items():    #튜플 형식으로 받기.
    print(s)
print()
for v in sugang.values():
    print(v)
