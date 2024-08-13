def menu_input():
    user_num = int(input("메뉴에서 필요하신 항목을 선택해주세요"))
    if user_num < 0 or user_num >= 6:
        print("없는 메뉴입니다. 다시 입력해주세요")
        menu_input()
    else: 
        return user_num
        