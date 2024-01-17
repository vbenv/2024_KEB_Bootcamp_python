drinks_foods = {"위스키" : "초콜릿", "와인" : "치즈", "소주" : "삼겹살", "고량주" : "양꼬치"}

#drink = input(drinks_foods.keys())
drinks_foods_keys = list(drinks_foods)
while True:
    menu = input(f'다음 술 중에 고르세요. \n1) {drinks_foods_keys[0]},  2) {drinks_foods_keys[1]},  3) {drinks_foods_keys[2]},  4) {drinks_foods_keys[3]},   5) 먹고 싶은 게 없네요.')
    if menu == '1': #숫자로 쓰면 안됨
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다.')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다.')
    elif menu == '3':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다.')
    elif menu == '4':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다.')
    elif menu == '5':
        print(f'다음에 또 오세요')
        break