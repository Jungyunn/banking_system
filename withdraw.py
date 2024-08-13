def withdraw_money():
    account_id = int(input())
    withdraw_money_ = int(input())

    for i in range(len(account_list)):
        if account_id == account_list[i]:
            if account_list[i].balance >= withdraw_money_:
                accoutnt_list[i].balance -= withdraw_money_
                print("출금완료")
                return
            else:
                print("잔액부족")
                return
            
    print("유효하지 않는 ID입니다.")
        